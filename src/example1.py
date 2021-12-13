import prediction
import dataset

views = int(input('Views: '))
likes = int(input('Likes: '))
print()

prediction_result = prediction.Predicted(dataset.views_per_like__like_percentage,  views/likes)
estimated_ratio = prediction_result.result
estimated_dislikes = round((estimated_ratio/100)*likes-likes)

print(f'Estimated like-to-dislike-ratio: {estimated_ratio}%')
print(f'Estimated dislikes: {estimated_dislikes}')

prediction_result.show()