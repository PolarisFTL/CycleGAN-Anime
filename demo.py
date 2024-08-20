from PIL import Image
import os
import io  # 添加对io模块的导入

def compress_image(input_folder, output_folder, target_size_kb=(50, 100)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('png', 'jpg', 'jpeg')):
            filepath = os.path.join(input_folder, filename)
            img = Image.open(filepath)
            
            # Initial quality setting
            quality = 95
            while True:
                # Save image to a BytesIO object to check the size
                img_bytes = io.BytesIO()
                img.save(img_bytes, format='JPEG', quality=quality)
                img_size_kb = img_bytes.tell() / 1024
                
                if img_size_kb <= target_size_kb[1]:
                    break
                else:
                    quality -= 5  # Decrease quality to reduce size
                    if quality < 5:
                        break  # Stop if quality is too low
            
            # Save the compressed image
            output_path = os.path.join(output_folder, filename)
            img.save(output_path, format='JPEG', quality=quality)

# Example usage
input_folder = 'E:\Graduate_Student\datasets\GAN\GTAV\images'
output_folder = 'E:\Graduate_Student\datasets\GAN\GTAV/a'
compress_image(input_folder, output_folder)
