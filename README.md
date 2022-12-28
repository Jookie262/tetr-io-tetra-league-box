<h2 align="center">
    🟥 Tetr.io Tetra League Stats 🟧
    <p align="center">
        <img alt="Action Status" src="https://github.com/Jookie262/tetr-io-tetra-league-box/actions/workflows/tetrio.yml/badge.svg">
    </p>
</h2>


> 📌✨ For more pinned-gist projects like this one, check out: https://github.com/matchai/awesome-pinned-gists

## 🎒 Prep Work

1. Create a new public GitHub Gist (https://gist.github.com/)
2. Create a token with the `gist` scope and copy it. (https://github.com/settings/tokens/new)
3. Copy the `API token`

## 🖥 Project Setup

1. Fork this repo
2. Go to your fork's `Settings` > `Secrets` > `Actions` > `New repository secret`

## 🤫 Environment Secrets

- **GH_TOKEN:** The GitHub token generated above.
- **GIST_ID:** The ID portion from your gist url:

  `https://gist.github.com/Jookie262/`**`5ab38d3a50636dd6e90b8fbabe6f5c36`**.

  (Alternatively this can be put directly in `.github/workflows/tetrio.yml` as it is public anyway.)
- **TETR_IO_USERNAME:** Your [tetr.io](https://tetr.io/) username. (This can also be put directly in the yml). 

    - **The username you need to put in TETR_IO_USERNAME is always in LOWERCASE**.

## 🪗 Additional Things
**Take Note:** Upon forking this project, the github actions will not automatically run. You need to manually go to actions tab and run it.

## ✨ Credits
This code was heavily inspired (mostly taken from) [@sciencepal's chess-com-box-py
](https://github.com/sciencepal/chess-com-box-py)