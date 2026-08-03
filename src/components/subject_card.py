import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    stats_html = ""
    if stats:
        pills = "".join(
            f'<span class="stat-pill"><b>{value}</b> {label}</span>'
            for icon, label, value in stats
        )
        stats_html = f'<div class="stat-pills">{pills}</div>'

    html = f"""
    <div class="subject-card">
        <h3>{name}</h3>
        <p class="meta">
            Code: <span class="code-badge">{code}</span>
            &nbsp;·&nbsp; Section: <strong>{section}</strong>
        </p>
        {stats_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()