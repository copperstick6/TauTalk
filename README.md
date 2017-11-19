# TransAmericaChallenge

# Winner of Earthack's (HackDFW) Transamerica Google Home Challenge

## Inspiration
TransAmerica wanted to have an automated conversation application to help them with leads in marketing. We delivered exactly that, and more!

## What it does
The first iteration of the application is exactly what was asked for in the sheet they gave us. With further iterations, we built a twilio calling system to call the user after a certain amount of time after their initial experience, and we also added some extra intents to handle some inquiries users might have about the product. We integrated twilio to call users after a certain amount of time, but we ran out of Twilio credits. We even have an API endpoint in which admins can upload custom brochures and information to custom intents.

## How we built it
We built it using twilio's API, Flask-Ask, Flask, and a little bit of smtpblib

## Challenges we ran into
We had problems with the Flask-ask documentation. It was really badly documented, and we had problems understanding how to implement many of the features

## Accomplishments that we're proud of
We're proud of the fact that we got it working so quickly, and it's really effective!

## What we learned
We learned to never trust rogue developers to write good documentation

## What's next for Trans-Alexa
World Domination! Perhaps a general template for an Alexa application that can be adopted by many different companies and users

When you set up the skill yourself, don't forget to Account Linking. Head over to the security panel for apps and games within Amazon's panel, a quick google search should help you find it. Get a client ID and secret. Your authorization URL is https://www.amazon.com/ap/oa and your access token URl is https://api.amazon.com/auth/o2/token. The scope is profile. The second redirect url should be added to your security panel.

