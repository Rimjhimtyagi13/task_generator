from utils.generator import generate_tasks
import streamlit as st


def show_generator():
    if "spec_history" not in st.session_state:
        st.session_state["spec_history"] = []

    if "latest_output" not in st.session_state:
        st.session_state["latest_output"] = ""

    if "edited_output" not in st.session_state:
        st.session_state["edited_output"] = ""

    st.title(" Generate Tasks")
    st.markdown("Fill in the details below to generate user stories and engineering tasks.")

    #  FORM --
    with st.form("feature_form"):
        feature_goal = st.text_area(
            "Feature Goal *",
            placeholder="What problem are you trying to solve?"
        )

        target_users = st.text_area(
            "Target Users *",
            placeholder="Who will use this feature?"
        )

        constraints = st.text_area(
            "Constraints (optional)",
            placeholder="Any technical, time, or business constraints?"
        )

        template = st.selectbox(
            "Template",
            ["Web Application", "Mobile Application", "Internal Tool"]
        )

        submitted = st.form_submit_button("Generate Tasks")

    #  VALIDATION ----
    if submitted:
        errors = []

        if not feature_goal.strip():
            errors.append("Feature goal cannot be empty.")

        if not target_users.strip():
            errors.append("Target users cannot be empty.")

        if errors:
            for error in errors:
                st.error(error)
            return

        st.info("Generating tasks...")

        output, error = generate_tasks(
            feature_goal,
            target_users,
            constraints,
            template
        )

        if error:
            st.warning(error)
            return

        # -------- SUCCESS --------
        st.success("Tasks generated successfully!")
        st.subheader("Generated Tasks")
        st.markdown(output)

        # Save outputs
        st.session_state["latest_output"] = output
        st.session_state["edited_output"] = output

        # Save to history
        st.session_state["spec_history"].insert(0, {
            "goal": feature_goal,
            "users": target_users,
            "constraints": constraints,
            "template": template,
            "output": output
        })

        # only last 5
        st.session_state["spec_history"] = st.session_state["spec_history"][:5]

    #EDIT SECTION 
    if st.session_state["latest_output"]:
        st.divider()
        st.subheader("Edit Tasks")

        edited_output = st.text_area(
            "You can edit the generated tasks below:",
            value=st.session_state["edited_output"],
            height=300
        )

        st.session_state["edited_output"] = edited_output

        st.subheader("Export")

        st.download_button(
            label="⬇ Download as Markdown",
            data=edited_output,
            file_name="tasks.md",
            mime="text/markdown"
        )
