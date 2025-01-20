// MealPlan.js
import React from 'react';

const MealPlan = ({ data }) => {
  // data is the entire object from your backend:
  // {
  //   "mealPlan": {
  //     "days": [...]
  //   },
  //   "shoppingList": [...]
  // }

  // Safely destructure
  const { mealPlan, shoppingList } = data || {};

  // Validate mealPlan and its structure
  if (!mealPlan || !Array.isArray(mealPlan.days)) {
    return <p>Brak poprawnych danych do wyświetlenia.</p>;
  }

  return (
    <div>
      <h2>Jadłospis na tydzień</h2>
      {mealPlan.days.map((day, dayIndex) => (
        <div key={dayIndex}>
          <h3>{day.day}</h3>
          {Array.isArray(day.meals) ? (
            day.meals.map((meal, mealIndex) => (
              <div key={mealIndex} style={{ marginBottom: '10px' }}>
                <p>
                  <strong>{meal.name}</strong> ({meal.time})
                </p>
                <p>
                  <strong>Składniki:</strong>{' '}
                  {meal.ingredients || 'Brak składników'}
                </p>
                <p>
                  <strong>Przepis:</strong>{' '}
                  {meal.recipe || 'Brak przepisu'}
                </p>
              </div>
            ))
          ) : (
            <p>Brak posiłków dla {day.day}</p>
          )}
        </div>
      ))}

      {Array.isArray(shoppingList) && shoppingList.length > 0 && (
        <>
          <h3>Lista zakupów:</h3>
          <ul>
            {shoppingList.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
};

export default MealPlan;
