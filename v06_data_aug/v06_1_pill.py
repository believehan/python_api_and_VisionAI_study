from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# 1. 이미지 로드
img = Image.open("v06_data_aug/data_aug.jpg")

# 2. 이미지 조정(회전)
img_rotated = img.rotate(90)
########################## + 3가지 데이터 증강 진행해서 이미지 시각화!!
# 이미지 흑백
bw = ImageEnhance.Color(img).enhance(0.1)
# 이미지 선명도
Sharpness = ImageEnhance.Sharpness(img).enhance(17)

# 3. 결과 시각화
fig, ax = plt.subplots(1,4, figsize=(10, 5))
# 3-1. 원본 이미지 시각화
ax[0].imshow(img)
ax[0].axis('off')
ax[0].set_title('Original')

# 3-2. 회전 이미지 시각화
ax[1].imshow(img_rotated)
ax[1].axis('off')
ax[1].set_title('Rotated')

# 3-3. 흑백 이미지 시각화
ax[2].imshow(bw)
ax[2].axis('off')
ax[2].set_title('black-White')

# 3-4. 선명도 이미지 시각화
ax[3].imshow(Sharpness)
ax[3].axis('off')
ax[3].set_title('Sharpness')

plt.show()
# 4. 결과 이미지 저장
