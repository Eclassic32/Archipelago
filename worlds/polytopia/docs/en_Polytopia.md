# The Battle Of Polytopia

[The Battle of Polytopia](https://store.steampowered.com/app/874390/) is a 2016 4X turn-based strategy game developed and published by Midjiwan AB. Players take control of a tribe as they build an empire and attempt to defeat the other tribes across a procedurally generated world. Each tribe starts the game with a unique ability, though all have access to the same technology tree. As players explore the world map, they construct and upgrade cities, research new technologies, and produce units used to battle the other tribes.

## Goal:
You need to play several matches with unique tribes, and reach `{RequiredScoreForVictory}` score on `{RequiredUniqueTribesWins}` unique tribes.

## Items:
- Tribe Unlock - `{TRIBE_NAME}`;
- Filler;

## Locations:
- `{TRIBE_NAME}` - Score `{from 1, up to 100}`K;
- `{TRIBE_NAME}` - Victory; 
> *// Note: Victory Location is sent only at the end of the match* 

## Options:
- **Playable Tribes** - Select which tribes are in your game. (default: first 12 tribes)
- **First Unlocked Tribe** - With which tribe you start the game, options: 16 tribes currently in game + 4 randomized options. (default: any playable tribe)
- **RequiredUniqueTribesWins** - How many *"`{TRIBE_NAME}` - Victory"* checks you need to goal your game. (default: 4)
- **RequiredScoreForVictory** - What score (in thousands) you need to check *"`{TRIBE_NAME}` - Victory"*. (default: 15)
- **ShouldSendScoreChecksImmediately** - Should Score Checks be sent immediately, or at the end of the match (default: true, immediately)
- **ScoreChecksMin** - Minimum score (in thousands) to create Score Checks. (default: 2)
- **ScoreChecksMax** - Maximum score (in thousands) to create Score Checks. (default: 20)
- **ScoreChecksStep** - Step size to create Score Checks. (default: 2)
> *// Note: Setting any of the Score Check options to 0 will disable them*
> Example: on default options these Score Checks are created: 2K, 4K, 6K, 8K, 10K, 12K, 14K, 16K, 18K, 20K

## AI Disclosure:
Small portion of the code was written by AI Inline Suggestions (GitHub Copilot), with carefull inspection of its code. No other generative AI was used in writing AP World. 