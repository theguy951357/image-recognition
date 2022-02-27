import logging
import fiftyone as fo
import fiftyone.zoo as foz
import fiftyone.utils.annotations as foua

logger = logging.getLogger(__name__)


class Manipulator:
    def __init__(self, config):
        self.config = config
        self.model = self.load_model()
        self.dataset = fo.Dataset.from_dir(
            dataset_dir=config.image_dir,
            dataset_type=fo.types.ImageDirectory
        )

        self.dataset.apply_model(self.model)

    def load_model(self, attempted=False):
        try:
            return foz.load_zoo_model("centernet-resnet50-v2-512-coco-tf2")
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
                "show_all_confidences": True,
                "per_object_label_colors": True
            }
        )
        self.dataset.draw_labels(self.config.out_dir, label_fields=None, config=cfg)
