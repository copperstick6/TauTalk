# TransAmericaChallenge

# Winner of Earthack's (HackDFW) Transamerica Google Home Challenge

Challenge Description:
TransAmerica - Google Home  
Build a Google Home lead capture conversational app.   
Winners will receive a Google Home.   
They said it was ok to build it with Alexa, so that's what I did. (I really don't like NodeJS, JavaScript confuses me, but I'll need to learn it someday. Today is not that day).

Built with Flask-Ask, the world's least documented, most used package for hardware in python

Test it out yourself! Use ngorok https://ngrok.com/ to expose your local server to alexa. move it to your local directory and run ./ngorok 5000 if you're using mac, and some other random command for inferior windows machines. Take that address and make sure your Alexa app points to that address.

When you set up the skill yourself, don't forget to Account Linking. Head over to the security panel for apps and games within Amazon's panel, a quick google search should help you find it. Get a client ID and secret. Your authorization URL is https://www.amazon.com/ap/oa and your access token URl is https://api.amazon.com/auth/o2/token. The scope is profile. The second redirect url should be added to your security panel.

