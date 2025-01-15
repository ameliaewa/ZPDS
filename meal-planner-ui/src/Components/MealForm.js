import React, { useState } from 'react';
import './MealForm.css'
// import DatePicker from 'react-datepicker';
// import 'react-datepicker/dist/react-datepicker.css';

const MealForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    budget: '',
    cookingTime: '',
    days: [],
    suggestMeals: false,
    mealsPerDay: 3,
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
          placeholder="Wpisz budżet w PLN"
        />
      </label>
      <br />

      <label>
        Czas na gotowanie (w minutach):
        <input
          type="number"
          name="cookingTime"
          value={formData.cookingTime}
          onChange={handleChange}
          placeholder="Czas na gotowanie"
        />
      </label>
      <br />

      <label>
        Dni tygodnia na gotowanie:
        <select
          multiple
          name="days"
          value={formData.days}
          onChange={(e) =>
            setFormData((prev) => ({
              ...prev,
              days: Array.from(e.target.selectedOptions, (option) => option.value),
            }))
          }
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
        Sugerowanie posiłków na dwa dni:
        <input
          type="checkbox"
          name="suggestMeals"
          checked={formData.suggestMeals}
          onChange={handleChange}
        />
      </label>
      <br />

      <label>
        Liczba dań dziennie:
        <input
          type="number"
          name="mealsPerDay"
          value={formData.mealsPerDay}
          onChange={handleChange}
          min="1"
          max="10"
        />
      </label>
      <br />

      <label>
        Liczba kalorii dziennie:
        <input
          type="number"
          name="caloriesPerDay"
          value={formData.caloriesPerDay}
          onChange={handleChange}
        />
      </label>
      <br />

      <label>
        Alergie pokarmowe (oddzielone przecinkami):
        <input
          type="text"
          name="allergies"
          value={formData.allergies}
          onChange={handleChange}
          placeholder="np. orzechy, mleko"
        />
      </label>
      <br />

      <label>
        Dieta:
        <select
          name="diet"
          value={formData.diet}
          onChange={handleChange}
        >
          <option value="">Wybierz...</option>
          <option value="vege">Wegetariańska</option>
          <option value="vegan">Wegańska</option>
          <option value="gluten-free">Bezglutenowa</option>
        </select>
      </label>
      <br />

      <label>
        Kuchnia świata (inspiracja):
        <input
          type="text"
          name="cuisine"
          value={formData.cuisine}
          onChange={handleChange}
          placeholder="np. włoska, azjatycka"
        />
      </label>
      <br />

      <label>
        Preferencje (co lubisz):
        <input
          type="text"
          name="preferences"
          value={formData.preferences}
          onChange={handleChange}
          placeholder="np. owoce morza, ostre potrawy"
        />
      </label>
      <br />

      <label>
        Posiłki do pracy:
        <input
          type="checkbox"
          name="workMeals"
          checked={formData.workMeals}
          onChange={handleChange}
        />
      </label>
      <br />

      <label>
        Ile czasu na przygotowanie śniadania (w minutach):
        <input
          type="number"
          name="breakfastTime"
          value={formData.breakfastTime}
          onChange={handleChange}
        />
      </label>
      <br />

      <label>
        Produkty w lodówce (oddzielone przecinkami):
        <textarea
          name="fridgeItems"
          value={formData.fridgeItems}
          onChange={handleChange}
          placeholder="np. jajka, masło, mleko"
        />
      </label>
      <br />

      <button type="submit">Wyślij formularz</button>
    </form>
  );
};

export default MealForm;
