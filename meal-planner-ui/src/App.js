import React, { useState } from 'react';
import MealForm from './Components/MealForm';
import MealPlan from './Components/MealPlan';
import PDFGenerator from './Components/PDFGenerator';

const App = () => {
  const [formData, setFormData] = useState(null);
  const [mealPlan, setMealPlan] = useState(null);

  const handleFormSubmit = (data) => {
    setFormData(data);
    // Tutaj możesz dodać logikę generowania jadłospisu
    const generatedMealPlan = generateMealPlan(data);
    setMealPlan(generatedMealPlan);
  };

  const generateMealPlan = (data) => {
    // Tu implementujesz logikę generowania jadłospisu
    return {
      days: [
        { day: 'Poniedziałek', meals: ['Śniadanie', 'Obiad', 'Kolacja'] },
        { day: 'Wtorek', meals: ['Śniadanie', 'Obiad', 'Kolacja'] },
        // Reszta dni...
      ],
      shoppingList: ['Chleb', 'Jabłka', 'Makaron'],
    };
  };

  return (
    <div className="App">
      <h1>Meal Planner</h1>
      {!formData ? (
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
