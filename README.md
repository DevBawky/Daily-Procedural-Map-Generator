# Daily Procedural Map Generator

> __"A customized GitHub Action for Technical Design Portfolio"__

This is a bot repository that automatically generates a procedural map every day.<br>
It was created to study and apply __Automation__ and __Procedural Content Generation (PCG)__ algorithms.

## How It Works

It generates organic looking cave maps using the __Cellular Automata__ algorithm.

1. __Initialization__: Randomly places walls (⬛) and floors (⬜) on a grid.
2. __Smoothing (Simulation)__: Checks the neighbors of each cell.
    * If neighbors > 4 walls -> The cell becomes a wall.
    * If neighbors < 4 walls -> The cell becomes a floor.
3. __Automation__: A Python script runs daily at 09:00 (KST) via GitHub Actions to update the section below.

## Getting Started

You can run the script locally to generate a map or fork this repository to run the automation on your own profile.

### 1. Run Locally
If you want to test the map generation algorithm on your local machine:

1. __Clone the repository__
   ```bash
   git clone [https://github.com/DevBawky/Daily-Procedural-Map-Generator.git](https://github.com/DevBawky/Daily-Procedural-Map-Generator.git)
   cd Daily-Procedural-Map-Generator
   ```
2. __Run the script__
   ```bash
   python generate_map.py
   ```

### 2. GitHub Actions Setup (For Forkers)
If you fork this repository, you must configure permissions and update the user info to allow the bot to commit changes.

#### Step 1: Configure Permissions
1. Go to __Settings__ > __Actions__ > __General__.
2. Scroll down to __Workflow permissions__.
3. Select __Read and write permissions__.
4. Click __Save__.

#### Step 2: Update Git Configuration
1. Open the `.github/workflows/main.yml` file.
2. Locate the `git config` part.
3. Replace the __user.email__ and __user.name__ with your own GitHub information.
   *(This ensures the daily commits are attributed to you.)*

The Action is scheduled to run daily. You can also manually trigger it via the __Actions__ tab.

## Tech Stack
* Language : Python 3.x
* CI/CD : Github Actions
* Algorithm : Cellular Automata for Cave Generation

<!-- DAILY_MAP_START -->
### Today's Generated Map (2025/12/30)
```
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬛
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛
⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛
⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛
⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
```
_By DevBawky_
<!-- DAILY_MAP_END -->