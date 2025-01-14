import React from 'react';

const MealPlan = ({ mealPlan }) => {
  return (
    <div>
      <h2>Jadłospis na tydzień</h2>
      <ul>
        {mealPlan.days.map((day, index) => (
          <li key={index}>
            <h3>{day.day}</h3>
            <ul>
              {day.meals.map((meal, idx) => (
                <li key={idx}>
                  {meal} - <button onClick={() => alert('Szczegóły posiłku')}>Pokaż szczegóły</button>
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
      <h3>Lista zakupów:</h3>
      <ul>
        {mealPlan.shoppingList.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  );
};

export default MealPlan;
