from gup.schemas import Detection, PerceptionResult


def test_perception_result_accepts_normalized_detection():
    result = PerceptionResult(
        game_id="example",
        frame_id=12,
        model_id="M01",
        detections=[
            Detection(
                class_name="player_hp",
                bbox_xyxy=(0.1, 0.8, 0.4, 0.84),
                value=0.75,
                confidence=0.98,
            )
        ],
    )
    assert result.detections[0].class_name == "player_hp"


def test_unknown_is_a_valid_status():
    result = PerceptionResult(game_id="unknown_game", model_id="M03", status="unknown")
    assert result.status == "unknown"
