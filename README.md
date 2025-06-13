# Aurora Discord Bot Tracker
## Overview
The Aurora Discord Bot Tracker is designed to provide real-time updates directly to Discord.

## Future Development Plans

[advisory-outlook](https://services.swpc.noaa.gov/text/advisory-outlook.txt)

[ovation_latest_aurora_n](https://services.swpc.noaa.gov/text/ovation_latest_aurora_n.txt)

[daily-geomagnetic-indices](https://services.swpc.noaa.gov/text/daily-geomagnetic-indices.txt)

[aurora-nowcast-hemi-power](https://services.swpc.noaa.gov/text/aurora-nowcast-hemi-power.txt)

[geospace_3_hour](https://services.swpc.noaa.gov/images/geospace/geospace_3_hour.png)

[geospace_pred_est_kp_1_hour](https://services.swpc.noaa.gov/json/geospace/geospace_pred_est_kp_1_hour.json)

[planetary_k_index_1m](https://services.swpc.noaa.gov/json/planetary_k_index_1m.json)

[ovation_aurora_latest](https://services.swpc.noaa.gov/json/ovation_aurora_latest.json)


# Running 

1.  Create and modify a file called `.env` with contents:

    ```bash
    DISCORD_TOKEN=token 

    ```
2. Launch the containers with the terminal.

    ```bash
    $ podman build -t discordbot -f Dockerfile

    $ podman run -d localhost/discordbot:latest
    ```