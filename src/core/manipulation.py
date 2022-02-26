# Functions for image manipulation, wrapped around FiftyOne
import fiftyone as fo
import fiftyone.zoo as foz
import fiftyone.utils.annotations as foua


class Manipulator:
    def __init__(self, config):
        self.config = config
        self.model = foz.load_zoo_model("centernet-resnet50-v2-512-coco-tf2")
        self.dataset = fo.Dataset.from_dir(
            dataset_dir=config.image_dir,
            dataset_type=fo.types.ImageDirectory
        )

        self.dataset.apply_model(self.model)

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

