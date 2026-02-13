from utils.generator import generate_tasks
import streamlit as st

def show_generator():

    #  Initialize session state once
    if "spec_history" not in st.session_state:
        st.session_state["spec_history"] = []

def show_generator():
    st.title("🛠️ Generate Tasks")

    st.markdown(
        "Fill in the details below to generate user stories and engineering tasks."
    )

    # for Form 
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

        # If validation passes
        st.success("Input looks good! (Task generation will happen next.)")

        # Temporary preview (for confidence & debugging)
        st.subheader("Your Input Summary")
        st.write("**Goal:**", feature_goal)
        st.write("**Users:**", target_users)
        st.write("**Constraints:**", constraints if constraints else "None")
        st.write("**Template:**", template)
        st.divider()

        st.info("Generating tasks...")

        output, error = generate_tasks(
            feature_goal,
            target_users,
            constraints,
            template
        )

        if error:
            st.warning(error)

        if output:
            st.success("Tasks generated successfully!")
            st.subheader("Generated Tasks")
            st.markdown(output)

            # Save output
            st.session_state["latest_output"] = output

            # Save to history
            st.session_state["spec_history"].insert(0, {
                "goal": feature_goal,
                "users": target_users,
                "constraints": constraints,
                "template": template,
                "output": output
            })

            # Keep last 5
            st.session_state["spec_history"] = st.session_state["spec_history"][:5]

