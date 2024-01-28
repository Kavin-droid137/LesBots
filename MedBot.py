import streamlit as st

# Define common diseases dictionary
common_diseases = {
    'flu': {
        'Symptoms': ['Fever', 'Cough', 'Fatigue', 'Muscle aches'],
        'Causes': ['Influenza viruses'],
        'Medicines': ['Antiviral medications (e.g., Oseltamivir)', 'Pain relievers (e.g., Acetaminophen)', 'Cough suppressants']
    },
    'common cold': {
        'Symptoms': ['Runny nose', 'Sneezing', 'Sore throat', 'Cough'],
        'Causes': ['Rhinoviruses', 'Coronaviruses'],
        'Medicines': ['Decongestants', 'Antihistamines', 'Cough syrups']
    },
    'migraine': {
        'Symptoms': ['Severe headaches', 'Nausea', 'Sensitivity to light'],
        'Causes': ['Genetics', 'Hormonal changes', 'Triggers like certain foods'],
        'Medicines': ['Pain relievers (e.g., Ibuprofen)', 'Triptans', 'Anti-nausea medications']
    },
    'alzheimers disease': {
        'Symptoms': ['Memory loss', 'Difficulty in problem-solving', 'Confusion'],
        'Causes': ['Genetics', 'Age-related changes in the brain'],
        'Medicines': ['Cholinesterase inhibitors (e.g., Donepezil)', 'Memantine']
    },
    'rheumatoid arthritis': {
        'Symptoms': ['Joint pain', 'Swelling', 'Fatigue'],
        'Causes': ['Autoimmune response'],
        'Medicines': ['Nonsteroidal anti-inflammatory drugs (NSAIDs)', 'Disease-modifying antirheumatic drugs (DMARDs)']
    },
    'chronic kidney disease': {
        'Symptoms': ['Fatigue', 'Swelling in extremities', 'Changes in urine output'],
        'Causes': ['Diabetes', 'High blood pressure', 'Kidney infections'],
        'Medicines': ['Blood pressure medications', 'Diuretics', 'Erythropoiesis-stimulating agents (ESA)']
    },
}

# Streamlit App
def display_disease_info(disease):
    if disease in common_diseases:
        disease_info = common_diseases[disease]
        st.success(f"**Description for {disease.capitalize()}**:")
        st.markdown(f"**Symptoms:** {', '.join(disease_info['Symptoms'])}")
        st.markdown(f"**Causes:** {', '.join(disease_info['Causes'])}")
        st.markdown(f"**Medication:** {', '.join(disease_info['Medicines'])}")
    else:
        st.error(f"Sorry, information not found for {disease}.")

def identify_disease_by_symptoms(symptoms):
    symptoms_lower = set(symptom.lower() for symptom in symptoms)
    possible_diseases = [disease for disease, info in common_diseases.items() if symptoms_lower.intersection(map(str.lower, info['Symptoms']))]
    return possible_diseases

def main():
    st.title("Medical ChatBot")
    st.sidebar.header("Options")
    option = st.sidebar.radio("Select an option:", ["Know about a disease", "Identify disease by symptoms"])

    if option == "Know about a disease":
        disease_to_describe = st.sidebar.selectbox("Select a disease:", list(common_diseases.keys()))
        display_disease_info(disease_to_describe)
    elif option == "Identify disease by symptoms":
        user_input = st.text_input("Enter the symptoms separated by commas:")
        provided_symptoms = [symptom.strip() for symptom in user_input.split(',')]
        possible_diseases = identify_disease_by_symptoms(provided_symptoms)
        if possible_diseases:
            st.success(f"**Based on the provided symptoms, it could be one or more of the following diseases:**")
            for disease in possible_diseases:
                display_disease_info(disease)
        else:
            st.error("Unable to identify the disease based on provided symptoms.")
    else:
        st.warning("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
