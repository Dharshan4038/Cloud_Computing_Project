import pandas as pd
import numpy as np
import pickle
import streamlit as st
import sklearn

pickle_in = open("dtree.pkl", "rb")
clf = pickle.load(pickle_in)


def predict_herb(l1):
    symptom = ['Immunity', 'Weight loss', 'Weight Gain',
               'Teeth and bone Strength', 'Knee pain/arthritis',
               'Blood detoxification', 'Infection and wounds', 'Body Pain',
               'Skin disease', 'Inactiveness', 'Gastric&Intestine troubles',
               'Hyperthermia or Fever', 'Diabetes', 'Cold,cough,throat infections',
               'Vision concerns', 'Nerve disorder', 'PCOS', 'Headache',
               'Respiratory concerns', 'Kidney & urinary problems', 'Heart problems',
               'Constipation', 'Diarrhoea', 'Liver', 'Male Reproductive concerns']

    lst = []
    for i in range(0, len(symptom)):
        lst.append(0)

    for j in range(0, len(l1)):
        for k in range(0, len(symptom)):
            if (l1[j] == symptom[k]):
                lst[k] = 1

    res1 = clf.predict([lst])
    herbs = ['Arugampul', 'Ashwagandha', 'Athimathuram', 'Arapu Leaves', 'Ammal Pacharisi', 'Athi Leaves', 'Arasu Leaves', 'Avuri Leaves', 'Arasu Seeds', 'Arasu pattai', 'Athi pattai', 'Amukura', 'Agraharam', 'Ashoka pattai', 'Aada Thodai', 'Aavaram Flowers', 'Aadu Theenda Palai', 'Avarai Panchangam', 'Aalamaram Seeds', 'Aalamaram pattai', 'Orange Peel', 'Aali Seeds', 'Aavarai Leaves', 'Lavangam pattai', 'Indhupu Flowers', 'Impural Flowers', 'Usilai', 'Oridhal Thamarai', 'Lemon Peel', 'Omam', 'Kandangkathiri', 'Kadukaai', 'Kasthuri Manjal', 'Curry Leaves', 'Karunjeeragam', 'Kabasura', 'Karungaali pattai', 'Karuvelam pattai', 'Kandanthipilli', 'Kalarchikaai', 'Kaasini Keerai', 'Kaarboga Arisi', 'Krambu', 'Keelanelli', 'Kuppaimeni', 'Kurunthotti Root', 'Koovai Kilangu', 'Kodi Veli', 'Kottai Karanthai', 'Guava Leaves', 'Korai Kilangu', 'Sadhakuppai', 'Srpagandha root', 'Sarkarai Kolli', 'Siru Thekkku', 'Sirukurinjaan', 'Siru Nerunjil', 'Siriyaanangai', 'Sitharathai', 'Siruthumbai leaves', 'Siruseruppadai', 'Sirupeelai', 'Sirupayaru', 'Sivanaar Vembu', 'Sivakaranthai', 'Seeragam', 'Seenthal kodi', 'Sukku', 'Surathu Nila aavarai', 'Surathu Nilaivaagai', 'Sembaruthi Flowers', 'Sabja seeds', 'Sevviyam', 'Aloe Vera', 'Thaneervittan Kilangu', 'Thaandri Kaai', 'Thaalisapathiri leaves', 'Thippli', 'Thiruneetru Pachilai', 'Thuthi Leaves', 'Tulsi Leaves',
             'Thuthi Seeds', 'Thudhuvalai', 'Thottal Sivungi', 'Devatharu', 'Thetran Kottai', 'Nannari', 'Nathai Soori', 'Naaval Seeds', 'Nayuruvi Leaves', 'Naval pattai', 'Naalpamaraathi', 'Nilavembu ', 'Nithya kalyani roots', 'Nithya kalyani leaves', 'Nilavaagai', 'Nilapanai kizhangu', 'Neermulli', 'Neermulli seeds', 'Neeli auri leaves', 'Nochi leaves', 'Nellikai', 'Parpadagam', 'Paal mudhingan', 'Parangi pattai', 'Pakarkai', 'Badham Pisin', 'Pirandai', 'Pudhina leaves', 'Boomi chakkarai kilangu', 'Poovasaram pattai', 'Poolangilangu', 'Poonai kaali vidhai', 'Ponkorandi root', 'Ponnagkanni', 'Manjal karisalaangkanni', 'Mara manjal ', 'Magilam flowers', 'Marutham pattai', 'Marudhani leaves', 'Manathakkali ', 'Maavilangapattai', 'Maathulai peel', 'Maasikkaai', 'Maamparupu', 'Milagu', 'Mudakkathan', 'Musumusukkai leaf', 'Murungai Vidhai', 'Murungai Poo', 'Murungai pisin', 'Murungai leaves', 'Multhani matti', 'Mookaratai saaranai', 'Yaanai nerinjil', 'Roja Idhazh ', 'Vallarai', 'Vasambu', 'Vatta thiruppi', 'Vaazhai thandu', 'Vaaivilangam', 'Vadhanarayanan', 'Vaadhamadakki', 'Vishnugranthi', 'Virali manjal', 'Vilvam leaves', 'Vellai karisalaangkanni', 'Vettiver', 'Vendhayam', 'Venthamarai flowers', 'Vellarugu', 'Vellari seeds', 'Veppam leaves', 'Veppam flowers', 'Veliparuthi', 'Veppam pattai', 'Jadhikkai', 'Tulsi seeds', 'Sembaruthi leaves', 'Shataveri']

    return herbs[int(res1)]


st.title("HerbWise: Herbal Medicine Crystal Ball")
html_temp = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Document</title>
                   
                </head>
                <body>
                    <div class="container">
                        <h2>HerbWise with Streamlit</h2>
                    </div>
                </body>
                </html>
            """


st.markdown(html_temp, unsafe_allow_html=True)
selected_option_1 = st.selectbox(
    "Symptom 1", ['Choose option', 'Immunity', 'Weight loss', 'Weight Gain', 'Teeth and bone Strength', 'Knee pain/arthritis', 'Blood detoxification', 'Infection and wounds', 'Body Pain', 'Skin disease', 'Inactiveness', 'Gastric&Intestine troubles', 'Hyperthermia or Fever',
                  'Diabetes', 'Cold, cough, throat infections', 'Vision concerns', 'Nerve disorder', 'PCOS', 'Headache', 'Respiratory concerns', 'Kidney & urinary problems', 'Heart problems', 'Constipation', 'Diarrhea', 'Liver', 'Male Reproductive concerns']
)
selected_option_2 = st.selectbox(
    "Symptom 2", ['Choose option', 'Immunity', 'Weight loss', 'Weight Gain', 'Teeth and bone Strength', 'Knee pain/arthritis', 'Blood detoxification', 'Infection and wounds', 'Body Pain', 'Skin disease', 'Inactiveness', 'Gastric&Intestine troubles', 'Hyperthermia or Fever',
                  'Diabetes', 'Cold, cough, throat infections', 'Vision concerns', 'Nerve disorder', 'PCOS', 'Headache', 'Respiratory concerns', 'Kidney & urinary problems', 'Heart problems', 'Constipation', 'Diarrhea', 'Liver', 'Male Reproductive concerns']
)
selected_option_3 = st.selectbox(
    "Symptom 3", ['Choose option', 'Immunity', 'Weight loss', 'Weight Gain', 'Teeth and bone Strength', 'Knee pain/arthritis', 'Blood detoxification', 'Infection and wounds', 'Body Pain', 'Skin disease', 'Inactiveness', 'Gastric&Intestine troubles', 'Hyperthermia or Fever',
                  'Diabetes', 'Cold, cough, throat infections', 'Vision concerns', 'Nerve disorder', 'PCOS', 'Headache', 'Respiratory concerns', 'Kidney & urinary problems', 'Heart problems', 'Constipation', 'Diarrhea', 'Liver', 'Male Reproductive concerns']
)
selected_option_4 = st.selectbox(
    "Symptom 4", ['Choose option', 'Immunity', 'Weight loss', 'Weight Gain', 'Teeth and bone Strength', 'Knee pain/arthritis', 'Blood detoxification', 'Infection and wounds', 'Body Pain', 'Skin disease', 'Inactiveness', 'Gastric&Intestine troubles', 'Hyperthermia or Fever',
                  'Diabetes', 'Cold, cough, throat infections', 'Vision concerns', 'Nerve disorder', 'PCOS', 'Headache', 'Respiratory concerns', 'Kidney & urinary problems', 'Heart problems', 'Constipation', 'Diarrhea', 'Liver', 'Male Reproductive concerns']
)
selected_option_5 = st.selectbox(
    "Symptom 5", ['Choose option', 'Immunity', 'Weight loss', 'Weight Gain', 'Teeth and bone Strength', 'Knee pain/arthritis', 'Blood detoxification', 'Infection and wounds', 'Body Pain', 'Skin disease', 'Inactiveness', 'Gastric&Intestine troubles', 'Hyperthermia or Fever',
                  'Diabetes', 'Cold, cough, throat infections', 'Vision concerns', 'Nerve disorder', 'PCOS', 'Headache', 'Respiratory concerns', 'Kidney & urinary problems', 'Heart problems', 'Constipation', 'Diarrhea', 'Liver', 'Male Reproductive concerns']
)

r1 = [selected_option_1, selected_option_2,
      selected_option_3, selected_option_4, selected_option_5]
result = ""
if st.button("Predict"):
    listn = []
    for i in r1:
        if i != "Choose option":
            listn.append(i)
    result = predict_herb(listn)

st.success("The suggested medicine is: {}".format(result))
