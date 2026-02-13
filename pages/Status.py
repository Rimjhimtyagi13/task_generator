import streamlit as st

def show_status():
    st.title("📊 System Status")

    st.success("Frontend: OK")
    st.success("Backend: OK")
    st.info("LLM: Mock mode")

    st.divider()
    st.subheader("🕒 Last Generated Specs")

    history = st.session_state.get("spec_history")

    if not history:
        st.info("No specs generated yet. Go to Generator page first.")
        return

    for idx, spec in enumerate(history, start=1):
        with st.expander(f"Spec #{idx}: {spec['goal'][:40]}"):
            st.write("**Users:**", spec["users"])
            st.write("**Constraints:**", spec["constraints"] or "None")
            st.write("**Template:**", spec["template"])
            st.markdown("### Generated Tasks")
            st.markdown(spec["output"])
