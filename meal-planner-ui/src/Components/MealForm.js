import React, { useState } from 'react';
import DatePicker from 'react-datepicker';
// import 'react-datepicker/dist/react-datepicker.css';

const MealForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    budget: '',
    cookingTime: '',
    days: [],
    suggestMeals: false,
    mealsPerDay: 1,
    caloriesPerDay: 2000,
    allergies: '',
    diet: '',
    cuisine: '',
    preferences: '',
    workMeals: false,
    breakfastTime: '',
    fridgeItems: '',
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Budżet:
        <input
          type="number"
          name="budget"
          value={formData.budget}
          onChange={handleChange}
        />
      </label>
      <br />

      <label>
        Czas na gotowanie:
        <input
          type="number"
          name="cookingTime"
          value={formData.cookingTime}
          onChange={handleChange}
        />
      </label>
      <br />

      <label>
        W jakie dni tygodnia gotujesz:
        <select
          multiple
          name="days"
          value={formData.days}
          onChange={handleChange}
        >
          <option value="Monday">Poniedziałek</option>
          <option value="Tuesday">Wtorek</option>
          <option value="Wednesday">Środa</option>
          <option value="Thursday">Czwartek</option>
          <option value="Friday">Piątek</option>
          <option value="Saturday">Sobota</option>
          <option value="Sunday">Niedziela</option>
        </select>
      </label>
      <br />

      <label>
        Sugerować posiłki na dwa dni?
        <input
          type="checkbox"
          name="suggestMeals"
          checked={formData.suggestMeals}
          onChange={handleChange}
        />
      </label>
      <br />

      {/* Inne pola formularza jak liczba posiłków, alergie, dieta, itd. */}

      <button type="submit">Wyślij formularz</button>
    </form>
  );
};

export default MealForm;
