import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog
from PIL import Image


def invert_colors(image_path, output_path):
    try:
        img = Image.open(image_path)
        inverted_image = Image.eval(img, lambda x: 255 - x)
        inverted_image.save(output_path)
        print("Image colors inverted and saved successfully.")
    except Exception as e:
        print(f"Error inverting colors: {e}")


class ImagePickerApp(QWidget):
    def __init__(self):
        super().__init__()

        self.image_path = None

        self.pick_image()

    def pick_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        self.image_path, _ = QFileDialog.getOpenFileName(self, "Pick an Image", "", "Image Files (*.png *.jpg *.bmp)")
        if self.image_path:
            output_path, _ = QFileDialog.getSaveFileName(self, "Save Inverted Image", "", "Image Files (*.png *.jpg *.bmp)")
            if output_path:
                invert_colors(self.image_path, output_path)
                self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImagePickerApp()
    window.setWindowTitle('Image Picker')
    sys.exit(app.exec_())