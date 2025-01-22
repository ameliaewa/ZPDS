// App.js
import React, { useState } from 'react';
import MealForm from './Components/MealForm';
import MealPlan from './Components/MealPlan';

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
        body: JSON.stringify(data),
      });
      
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      // Wait for the full JSON response
      const result = await response.json();

      
      setFormData(data);
      setMealPlan(result.received_data);

    } catch (error) {
      console.error('Error:', error);
      alert('Failed to process meal plan'); 
    } finally {
      // Turn off loading after we get a response or an error
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Weekly Meal Planner</h1>

      {/* 1) If we are loading, show a spinner or text */}
      {isLoading && <p>Generating your meal plan, please wait...</p>}

      {/* 2) If not loading and we haven't submitted form data, show the form */}
      {!isLoading && !formData && (
        <MealForm onSubmit={handleFormSubmit} />
      )}

      {/* 3) If not loading and we have formData + mealPlan, show the plan */}
      {!isLoading && formData && mealPlan && (
        <MealPlan 
        data={mealPlan} 
        formData={formData} // Pass the formData to use in the MealPlan
        onResubmit={handleFormSubmit} // Pass the function for resubmission
        />
      )}
    </div>
  );
};

export default App;
