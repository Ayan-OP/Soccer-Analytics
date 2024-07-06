# Soccer Analysis using YOLOv8

Recently, the World Cup took place, with Argentina coming out on top as the champion. The tournament brought joy and excitement to fans all over the world, and it’s no surprise that many of them are looking for new ways to enhance their viewing experience.

This is where **YOLO** and **Computer Vision** come in. By using these technologies, it’s possible to track and analyze the movements of individual players on the field in real time. This can be incredibly useful for both fans and coaches, as it allows for a deeper understanding of the game and the strategies used by different teams. 

This project employs YOLO (You Only Look Once) object detection to conduct comprehensive analysis of football matches. The goal is to provide detailed insights into player performance, team dynamics, ball possession, and camera movements during a match.

<p><img height="300" width="500" src="https://github.com/Ayan-OP/Soccer-Analytics/blob/main/input_videos/input_video_gif.gif" title="Input Video" alt="demo">
<img height="300" width="500" src="https://github.com/Ayan-OP/Soccer-Analytics/blob/main/output_videos/output_video_gif.gif" title="Processed Video" alt="demo"></p>


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Ayan-OP/Soccer-Analytics.git
   cd Soccer-Analytics
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

The following libraries are used in this project:

- ultralytics
- opencv-python
- supervision
- scikit-learn
- roboflow
- numpy
- pandas
- pickle
- shutil

## Usage

1. **Data Preparation:**

   - Place your video footage of the football match in the `input_videos` directory.

2. **Running the Analysis:**

   - Execute the main script `python main.py` to initiate the analysis process.
   - The analysis encompasses the following key steps:
     - Object tracking using YOLO for players, referees, and the football.
     - Estimating camera movements to understand viewpoint changes.
     - Calculating player speed, distance traveled, and determining ball possession.
     - Visualizing analysis results on the video frames.

3. **Output:**
   - The annotated and analyzed video will be saved in the `output_videos` directory for review.

## Code Structure

- **`utils.py`**: Contains utility functions for video I/O operations.
- **`trackers.py`**: Implements the **Supervision byte tracker** and interpolation techniques to track players, referees and the ball.
- **`team_assigner.py`**: Assigns teams to players using **KMeans clustering** based on their visual appearance. <img height="50" width="50" src="https://github.com/Ayan-OP/Soccer-Analytics/blob/main/team_assigner/1_4I8poHyYgGXgRfX6h6xbbA.jpg" title="Processed Video" alt="demo">
- **`player_ball_assigner.py`**: Determines ball possession among players during the match.
- **`camera_movement_estimator.py`**: Estimates camera movements to analyze perspective changes.
- **`view_transformer.py`**: Transforms object positions based on the camera view for accurate analysis.
- **`speed_and_distance_estimator.py`**: Calculates player speeds and distances traveled for performance evaluation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the YOLOv8 team and the contributors of the libraries used in this project for their valuable contributions to the field of object detection and analysis in computer vision.
