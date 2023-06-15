from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Salary
from .serializers import SalaryInputSerializer
from .preprocess import preprocess_data
import pickle
import warnings


warnings.filterwarnings("ignore", category=UserWarning)


class SalaryPredictionView(APIView):
    def post(self, request):
        # Load the trained model from the pickle file
        with open('./ml/salary_model.pkl', 'rb') as f:
            model = pickle.load(f)

        # Preprocess the input data
        input_data = request.data
        preprocessed_data = preprocess_data(input_data)

        # Make a prediction using the preprocessed input data
        prediction = model.predict([list(preprocessed_data.values())])

        # Save the salary data and prediction to the database
        salary = Salary(YearsExperience=input_data['YearsExperience'],
                        salary=prediction[0])
        salary.save()

        # Serialize the input data and prediction to return as a response
        serializer = SalaryInputSerializer(data=input_data)
        if serializer.is_valid():
            response_data = serializer.data
            response_data['salary'] = prediction[0]
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)