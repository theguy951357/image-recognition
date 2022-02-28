import logging
import fiftyone as fo
import fiftyone.zoo as foz
import fiftyone.utils.annotations as foua

logger = logging.getLogger(__name__)


class Manipulator:
    def __init__(self, config):
        self.config = config
        self.model = self.load_model()
        self.image_dataset = fo.Dataset.from_dir(
            dataset_dir=config.image_dir,
            dataset_type=fo.types.ImageDirectory
        )
        self.video_dataset = fo.Dataset.from_dir(
            dataset_dir=config.video_dir,
            dataset_type=fo.types.VideoDirectory
        )

        self.image_dataset.apply_model(self.model)
        self.video_dataset.apply_model(self.model)

    def load_model(self, attempted=False):
        try:
            return foz.load_zoo_model("ssd-inception-v2-coco-tf")

        except (ModuleNotFoundError, ImportError) as e:
            if attempted:
                raise e

            logger.warning(f'Exception handled: {type(e)} -- Attempting to install eta models.')

            import os
            os.system('eta install models')

            return self.load_model(True)

    def export(self):
        cfg = foua.DrawConfig(
            {
                "font_size": 14,
                "bbox_linewidth": 3,
                "bbox_alpha": 0.82,
                "per_object_label_colors": True,
                "show_object_confidences": True,
            }
        )
        self.image_dataset.draw_labels(self.config.out_dir, label_fields=None, config=cfg)
        self.video_dataset.draw_labels(self.config.out_dir, label_fields=None, config=cfg)
