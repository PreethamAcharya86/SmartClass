import io
import numpy as np
import librosa
import streamlit as st
import torch
import torch.nn.functional as F
import traceback
from speechbrain.pretrained import EncoderClassifier

@st.cache_resource
def load_voice_encoder():
    return EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-ecapa-voxceleb",
        savedir="pretrained_models/spkrec-ecapa-voxceleb"
    )


def preprocess_wav(audio):
    audio = np.asarray(audio, dtype=np.float32)

    if len(audio) == 0:
        return audio

    peak = np.max(np.abs(audio))

    if peak > 0:
        audio = audio / peak

    return audio


def get_voice_embedding(audio_bytes):
    try:
        st.write("Loading encoder...")
        encoder = load_voice_encoder()

        st.write("Audio bytes:", len(audio_bytes))

        audio, sr = librosa.load(
            io.BytesIO(audio_bytes),
            sr=16000,
            mono=True
        )

        st.write("Audio shape:", audio.shape)
        st.write("Sample rate:", sr)

        wav = preprocess_wav(audio)

        waveform = torch.tensor(
            wav,
            dtype=torch.float32
        ).unsqueeze(0)

        st.write("Waveform:", waveform.shape)

        embedding = encoder.encode_batch(waveform)

        st.write("Embedding:", embedding.shape)

        return embedding.squeeze().cpu().numpy().tolist()

    except Exception:
        import traceback
        st.exception(traceback.format_exc())
        return None

def process_bulk_audio(audio_bytes, candidates_dict, threshold=0.65):

    try:

        encoder = load_voice_encoder()

        audio, sr = librosa.load(
            io.BytesIO(audio_bytes),
            sr=16000,
            mono=True
        )

        segments = librosa.effects.split(
            audio,
            top_db=30
        )

        identified_results = {}

        for start, end in segments:

            if (end - start) < sr * 0.5:
                continue

            segment_audio = audio[start:end]

            wav = preprocess_wav(segment_audio)

            waveform = torch.tensor(
                wav,
                dtype=torch.float32
            ).unsqueeze(0)

            embedding = encoder.encode_batch(waveform)

            embedding = embedding.squeeze().detach().cpu().numpy()

            sid, score = identify_speaker(
                embedding.tolist(),
                candidates_dict,
                threshold
            )

            if sid:

                if (
                    sid not in identified_results or
                    score > identified_results[sid]
                ):
                    identified_results[sid] = score

        return identified_results

    except Exception as e:
        st.error(f"Bulk process error: {e}")
        return {}