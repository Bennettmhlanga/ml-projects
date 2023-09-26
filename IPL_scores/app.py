import streamlit as st
import pickle
import pandas as pd

# Load the pre-trained model
model_path = 'IPL_scores/lr-model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Transform team names into model-understood format
team_mapping = {
    'Chennai Super Kings': 'bat_team_Chennai Super Kings',
    'Delhi Daredevils': 'bat_team_Delhi Daredevils',
    'Kings XI Punjab': 'bat_team_Kings XI Punjab',
    'Kolkata Knight Riders': 'bat_team_Kolkata Knight Riders',
    'Mumbai Indians': 'bat_team_Mumbai Indians',
    'Rajasthan Royals': 'bat_team_Rajasthan Royals',
    'Royal Challengers Bangalore': 'bat_team_Royal Challengers Bangalore',
    'Sunrisers Hyderabad': 'bat_team_Sunrisers Hyderabad'
}

def transform_team_name(team_name):
    return team_mapping[team_name]

# Function to make predictions
def make_prediction(batting_team, bowling_team, overs, runs, wickets, runs_last_5, wickets_last_5):
    data = {
        'bat_team_Chennai Super Kings': [1 if batting_team == 'Chennai Super Kings' else 0],
        'bat_team_Delhi Daredevils': [1 if batting_team == 'Delhi Daredevils' else 0],
        'bat_team_Kings XI Punjab': [1 if batting_team == 'Kings XI Punjab' else 0],
        'bat_team_Kolkata Knight Riders': [1 if batting_team == 'Kolkata Knight Riders' else 0],
        'bat_team_Mumbai Indians': [1 if batting_team == 'Mumbai Indians' else 0],
        'bat_team_Rajasthan Royals': [1 if batting_team == 'Rajasthan Royals' else 0],
        'bat_team_Royal Challengers Bangalore': [1 if batting_team == 'Royal Challengers Bangalore' else 0],
        'bat_team_Sunrisers Hyderabad': [1 if batting_team == 'Sunrisers Hyderabad' else 0],
        'bowl_team_Chennai Super Kings': [1 if bowling_team == 'Chennai Super Kings' else 0],
        'bowl_team_Delhi Daredevils': [1 if bowling_team == 'Delhi Daredevils' else 0],
        'bowl_team_Kings XI Punjab': [1 if bowling_team == 'Kings XI Punjab' else 0],
        'bowl_team_Kolkata Knight Riders': [1 if bowling_team == 'Kolkata Knight Riders' else 0],
        'bowl_team_Mumbai Indians': [1 if bowling_team == 'Mumbai Indians' else 0],
        'bowl_team_Rajasthan Royals': [1 if bowling_team == 'Rajasthan Royals' else 0],
        'bowl_team_Royal Challengers Bangalore': [1 if bowling_team == 'Royal Challengers Bangalore' else 0],
        'bowl_team_Sunrisers Hyderabad': [1 if bowling_team == 'Sunrisers Hyderabad' else 0],
        'overs': [overs],
        'runs': [runs],
        'wickets': [wickets],
        'runs_last_5': [runs_last_5],
        'wickets_last_5': [wickets_last_5]
    }

    df = pd.DataFrame(data)
    prediction = model.predict(df)[0]
    return prediction

# Streamlit app
def main():
    st.title('IPL Score Prediction')

    # Select batting and bowling teams
    batting_team = st.selectbox('Batting Team', list(team_mapping.keys()), key='batting_team')
    bowling_team = st.selectbox('Bowling Team', list(team_mapping.keys()), key='bowling_team')

    # Input features
    overs = st.number_input('Overs', key='overs')
    runs = st.number_input('Runs', key='runs')
    wickets = st.number_input('Wickets', key='wickets')
    runs_last_5 = st.number_input('Runs in Last 5 Overs', key='runs_last_5')
    wickets_last_5 = st.number_input('Wickets in Last 5 Overs', key='wickets_last_5')

    # Make prediction
    if st.button('Predict'):
        prediction = make_prediction(batting_team, bowling_team, overs, runs, wickets, runs_last_5, wickets_last_5)
        st.success('Predicted Total Score: {:.2f}'.format(prediction))

if __name__ == '__main__':
    main()
