# Dining-Concierge-Bot

Built a Dining Concierge chatbot that sends the user restaurant suggestions given a set of preferences that the user provides the chatbot with through conversation.

Based on a conversation with the customer, the LEX chatbot will identify the user’s preferred ‘cuisine’. Afterwards, the ElasticSearch will get random 
suggestions of restaurant IDs with this cuisine. Then, DynamoDB table will be queried with these restaurant IDs to find more information about the restaurants 
that are being suggested to the customers like name and address of the restaurant. 

<img src="https://github.com/pelincetin/Dining-Concierge-Bot/blob/main/architecture.png" alt="Your image title" width="400"/>
