README.md
=========

Last edited: 2022-11-15 02:02:13

Contents:

.. code-block:: md

    <a href="https://discord.gg/metaplex"><img src="https://img.shields.io/discord/848060988636921856?color=5865F2&logo=discord&logoColor=white" alt="Discord server" /></a>
# Larry the Metaplex Discord Bot 

## Getting started: 
1. Clone the repo and run `yarn install`
    ```bash
    $ git clone https://github.com/metaplex-foundation/larry-discord-bot.git
    $ cd larry-discord-bot
    $ yarn install
    ```
2. Duplicate the `.env.example` file and rename it `.env`
3. Fill in the placeholders in the `.env` file with your credentials
4. To run the Docs Bot
    ```bash
    $ yarn run docs-bot
    ```
5. To run the Mod Bot:
    ```bash
    $ yarn run mod-bot
    ```

---
## The Docs Bot: 
The first bot allows you to hook into any Algolia DocSearch index and uses the interaction autocomplete functionality to make it easy for users to query documentation. 
>TODO:
> - [ ] Add functionality to store custom FAQs on a per-server basis
> - [ ] Convert the docs commands to a class and enable servers to deploy their own docs commands with an Algolia index and key 

---
## The Mod Bot:
The mod bot does a number of things:
- check members on join and compares their username to that of the moderation team of a server (configurable on a per-server basis). If it matches, the user is immediately kicked and the team is alerted. 
- get a list of probable bots in a server, and can perform bulk actions (kick/ban) on all of them.
- A number of other helpful things.
>TODO:
> - [ ]  Finish this bot


