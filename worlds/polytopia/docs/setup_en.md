# Setting up The Battle of Polytopia Archipelago

## Requirements:
- Archipelago Launcher
- Polytopia AP World

- Copy of The Battle of Polytopia on Steam
- Polymod
- Client-side Mod
> Epic build of the game is not tested, but should work regardless

> Mobile builds are not supported, for a reason of not having Polymod

## Generation:
1. Install `polytopia-VERSION.apworld` by putting it into `Archipelago Launcher` window, or by double-clicking
2. Go To `Archipelago Launcher` > `Generate Template Options` > `The Battle of Polytopia.yaml` > Change it > Move the YAML into parent `/Players` folder
3. Go To `Archipelago Launcher` > `Generate` > Open the `/output` folder
4. Host the new file either in https://archipelago.gg/uploads or `Archipelago Launcher` > `Host`

## Setting up the client-side mod:
1. Install The Battle of Polytopia from Steam and launch at least once
2. Open the folder where the game is (in Steam > Right Mouse Button on `The Battle of Polytopia` > `Properties...` > `Installed files` > `Browse...`)
3. Download Polymod Installer from https://polymod.dev/ and open it (Windows Defender might have issue with it, press `More Info...` > `Execute Anyway`)
4. Copy the folder address from Step 2 into `Game Path` > Press `Install`
5. Download client-side mod (`polytopia-AP_VERSION.polymod`) and place it in `...\The Battle of Polytopia\Mods`

## Connecting to the server:
1. In Main Menu, on top-left side of the screen, press `Archipelago Hub` button
2. Enter server address and port, slot name, password and press `CONNECT` 
3. On pressing `New Game` you will be sent to "Creative Mode" 
4. In Tribe Screen you can choose your tribe and start playing. Few notes:
  - Tribes NOT in your `Playable Tribes` **will not be displayed** at all, and can not be choosen neither by player or bot
  - Tribes you have YET TO RECEIVE have **red** background, and can not be choosen neither by player or bot
  - Tribes you received have default **blue** background, and can be choosen both by you and bot
  - Tribes you received, but DISABLED will have default **black** background, they can be re-enabled and can not be chosen by player or bot while disabled
  - (NOT IMPLEMENTED) Tribes you have checked Victory location will have **green** background
  - (NOT IMPLEMENTED) Tribes you have checked ALL location will have **gold** background
5. To Disconnect, in main menu press `Archipelago Hub` button and `DISCONNECT` button