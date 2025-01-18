// App.js
import React, { useState } from 'react';
import MealForm from './Components/MealForm';
import MealPlan from './Components/MealPlan';
import PDFGenerator from './Components/PDFGenerator';

const App = () => {
  const [formData, setFormData] = useState(null);
  const [mealPlan, setMealPlan] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleFormSubmit = async (data) => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/api/process-meal-plan/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
      });
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      
      const result = await response.json();
      setFormData(data);
      setMealPlan(result.received_data);
    } catch (error) {
      console.error('Error:', error);
      alert('Failed to process meal plan');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Weekly Meal Planner</h1>
      {isLoading ? (
        <p>Processing your meal plan...</p>
      ) : !formData ? (
        <MealForm onSubmit={handleFormSubmit} />
      ) : (
        <>
          <MealPlan mealPlan={mealPlan} />
          <PDFGenerator mealPlan={mealPlan} />
        </>
      )}
    </div>
  );
};

export default App;