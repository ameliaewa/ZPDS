// App.js
import React, { useState } from 'react';
import MealForm from './Components/MealForm';
import MealPlan from './Components/MealPlan';
import PDFGenerator from './Components/PDFGenerator';

const App = () => {
  const [formData, setFormData] = useState(null);
  const [mealPlan, setMealPlan] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFormSubmit = async (data) => {
    setLoading(true);
    setError(null);
    try {
      console.log('Sending data:', data); // Debug log
      const response = await fetch('http://localhost:8000/api/generate-meal-plan/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`Server responded with ${response.status}: ${errorText}`);
      }

      const mealPlanData = await response.json();
      setFormData(data);
      setMealPlan(mealPlanData);
    } catch (err) {
      console.error('Fetch error:', err); // Debug log
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Weekly Meal Planner</h1>
      {error && <div className="error">{error}</div>}
      {loading ? (
        <div>Generating your meal plan...</div>
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