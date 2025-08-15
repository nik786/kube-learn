import os
import warnings
import torch
from transformers import pipeline

# Suppress logs
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
warnings.filterwarnings("ignore")

# Force CPU usage
torch.cuda.is_available = lambda: False
torch.set_num_threads(4)

# Load pipeline


summarizer = pipeline(task="summarization",model="Falconsai/text_summarization")

news = """ Even as the decision to omit Shreyas Iyer and Ishan Kishan from the central contracts list for not turning up for domestic tournaments continues to receive mixed reactions, there was plenty of discussion about Hardik Pandya’s inclusion as well. The Indian Express understands that the selectors and the BCCI only handed Hardik a contract after the all-rounder gave an undertaking that if there are no white-ball commitments with the national team, he would feature for Baroda in the Syed Mushtaq Ali T20s and Vijay Hazare Trophy.

During the recent meeting, apart from Shreyas and Ishan, there was discussion regarding Pandya’s place in Grade A of the annual contract list as well. Since injuring his ankle during the World Cup in October, Pandya had remained out of action till last week when he returned to competitive cricket in the DY Patil tournament, where he is turning out for Reliance. Like Ishan, Pandya has been training individually in Vadodara, but what worked in his favour is that he has been reporting at the National Cricket Academy (NCA) on a time-to-time basis to have his fitness assessed.

According to a top BCCI official, Pandya has also given assurance that he would feature in domestic tournaments if they don’t overlap with international commitments. “We have had discussions with Pandya, who has been told to play domestic white-ball tournaments when he is available. At this stage, according to the assessment of the BCCI’s medical team, he is not in a position to bowl in red-ball tournaments. So playing Ranji Trophy is out of the equation for Pandya. But he has to play other white-ball tournaments if there are no India commitments. If not, he will miss out on a contract,” the official told The Indian Express.

According to the Future Tours Programme, India are scheduled to play only three T20Is at home against Bangladesh as the team has a busy Test calendar. In the October-December period, when India don’t have any white-ball commitments, the Syed Mushtaq Ali T20s and Vijay Hazare Trophy would be conducted. And unless Pandya has any fitness issues, he has been directed to feature in both these tournaments.

Different yardsticks
While former cricketers have welcomed the BCCI’s decision to drop Shreyas and Ishan from the contracts list, Irfan Pathan raised the question regarding Pandya on X (previously Twitter). “They are talented cricketers, both Shreyas and Ishan. Hoping they bounce back and come back stronger. If players like Hardik don’t want to play red-ball cricket, should he and others like him participate in white-ball cricket when they aren’t on national duty? If this doesn’t apply to all, then Indian cricket won’t achieve the desired results!” Pathan tweeted on Thursday morning.

Festive offer
Also Read | How missing Ranji Trophy games resulted in Shreyas Iyer and Ishan Kishan being dropped from BCCI’s central contract list
It is understood that the BCCI will also instruct contracted players to report to their respective state units when they are not part of the national team set-up. There have been instances when in the middle of the domestic season, players from several states attended short camps with their respective IPL franchises, a move which didn’t go down well with the state units. Shreyas, for instance, attended a Kolkata Knight Riders camp after missing a Ranji fixture with Mumbai.



On Wednesday, based on the recommendations of the selectors, BCCI secretary Jay Shah announced that Shreyas and Ishan were not considered for the 2023-24 annual contracts. Though the two were part of the national set-up across all three formats for the majority of 2023, that the duo didn’t turn up for Ranji Trophy had drawn sharp criticism from several quarters. And despite Shah writing to contracted players, urging them to participate in the tournament, Shreyas and Ishan missed the next round of Ranji fixtures.
"""
summarizer(news)



