import React, { useState } from 'react';
import '../App.css'; // Import your CSS file

const MealPlan = ({ data, formData, onResubmit }) => {
  const { mealPlan, shoppingList } = data || {};
  const [visibleMeals, setVisibleMeals] = useState({}); // Track visibility of meal details

  if (!mealPlan || !Array.isArray(mealPlan.days)) {
    return (
      <div className="App-header">
        <p>Brak poprawnych danych do wyświetlenia.</p>
      </div>
    );
  }

  const toggleMealDetails = (dayIndex, mealIndex) => {
    setVisibleMeals((prev) => ({
      ...prev,
      [dayIndex]: {
        ...prev[dayIndex],
        [mealIndex]: !prev[dayIndex]?.[mealIndex],
      },
    }));
  };

  const handleResubmit = () => {
    if (formData) {
      onResubmit(formData);
    } else {
      alert('No previous data to resubmit');
    }
  };

  return (
    <div style={{ padding: '20px', background: 'linear-gradient(to bottom, #f0fff4, #e8f5e9)' }}>
      <h2 style={{ color: '#4CAF50', fontSize: '28px', textAlign: 'center', marginBottom: '20px' }}>
        Jadłospis na tydzień
      </h2>
      <button
        onClick={handleResubmit}
        style={{
          display: 'block',
          margin: '0 auto 20px auto',
          backgroundColor: '#388E3C',
          color: '#fff',
          border: 'none',
          padding: '12px 20px',
          borderRadius: '8px',
          cursor: 'pointer',
          fontSize: '16px',
          boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
        }}
      >
        Wygeneruj ponownie
      </button>
      {mealPlan.days.map((day, dayIndex) => (
        <div
          key={dayIndex}
          style={{
            border: '1px solid #ddd',
            borderRadius: '12px',
            padding: '20px',
            marginBottom: '20px',
            backgroundColor: '#ffffff',
            boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
          }}
        >
          <h3 style={{ color: '#2C5F2D', fontSize: '24px', marginBottom: '15px' }}>{day.day}</h3>
          {Array.isArray(day.meals) && day.meals.length > 0 ? (
            day.meals.map((meal, mealIndex) => (
              <div
                key={mealIndex}
                style={{
                  marginBottom: '15px',
                  padding: '10px',
                  borderRadius: '8px',
                  backgroundColor: '#f9f9f9',
                  border: '1px solid #e0e0e0',
                }}
              >
                <p style={{ fontSize: '18px', marginBottom: '10px' }}>
                  <strong>{meal.name}: </strong>
                  <span style={{ color: '#4CAF50' }}>{meal.meal}</span> ({meal.time})
                </p>
                <button
                  className="download-button"
                  onClick={() => toggleMealDetails(dayIndex, mealIndex)}
                  style={{
                    backgroundColor: '#4CAF50',
                    color: '#fff',
                    border: 'none',
                    padding: '8px 12px',
                    borderRadius: '5px',
                    cursor: 'pointer',
                    fontSize: '14px',
                  }}
                >
                  {visibleMeals[dayIndex]?.[mealIndex] ? 'Ukryj szczegóły' : 'Pokaż szczegóły'}
                </button>
                {visibleMeals[dayIndex]?.[mealIndex] && (
                  <div style={{ marginTop: '10px', lineHeight: '1.5' }}>
                    <p>
                      <strong>Składniki:</strong> {meal.ingredients || 'Brak składników'}
                    </p>
                    <p>
                      <strong>Przepis:</strong> {meal.recipe || 'Brak przepisu'}
                    </p>
                  </div>
                )}
              </div>
            ))
          ) : (
            <p>Brak posiłków dla {day.day}</p>
          )}
        </div>
      ))}

      {Array.isArray(shoppingList) && shoppingList.length > 0 && (
        <div
          style={{
            marginTop: '30px',
            borderTop: '2px solid #4CAF50',
            paddingTop: '20px',
          }}
        >
          <h3 style={{ color: '#4CAF50', fontSize: '24px' }}>Lista zakupów:</h3>
          <ul style={{ listStyleType: 'none', padding: 0 }}>
            {shoppingList.map((item, index) => (
              <li
                key={index}
                style={{
                  background: '#e8f5e9',
                  marginBottom: '8px',
                  padding: '10px 15px',
                  borderRadius: '8px',
                  boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.1)',
                  fontSize: '16px',
                }}
              >
                {item}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default MealPlan;
