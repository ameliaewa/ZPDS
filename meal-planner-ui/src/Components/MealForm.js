import React, { useState } from 'react';
import './MealForm.css'

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

  const handleDayChange = (e) => {
    const { value, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      days: checked
        ? [...prev.days, value]
        : prev.days.filter((day) => day !== value),
    }));
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    const dataString = `
    Budget: ${formData.budget}
    Cooking Time: ${formData.cookingTime}
    Days: ${formData.days.join(', ')}
    Suggest Meals: ${formData.suggestMeals}
    Meals Per Day: ${formData.mealsPerDay}
    Calories Per Day: ${formData.caloriesPerDay}
    Allergies: ${formData.allergies}
    Diet: ${formData.diet}
    Cuisine: ${formData.cuisine}
    Preferences: ${formData.preferences}
    Work Meals: ${formData.workMeals}
    Breakfast Time: ${formData.breakfastTime}
    Fridge Items: ${formData.fridgeItems}
  `; //do wywalenia

    alert(dataString); // do wywalenia
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
          onInput={(e) => {
            e.target.value = e.target.value.replace(/[^0-9]/g, '');
          }}
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
          onInput={(e) => {
            e.target.value = e.target.value.replace(/[^0-9]/g, '');
          }}
        />
      </label>
      <br />

      <label>
        Dni tygodnia na gotowanie:
        <div className="checkbox-container">
            <label className="checkbox-label">
            <input
                type="checkbox"
                value="Monday"
                checked={formData.days.includes("Monday")}
                onChange={handleDayChange}
            />
            Poniedziałek
            </label>
            <label className="checkbox-label">
            <input
                type="checkbox"
                value="Tuesday"
                checked={formData.days.includes("Tuesday")}
                onChange={handleDayChange}
            />
            Wtorek
            </label>
            <label className="checkbox-label">
            <input
                type="checkbox"
                value="Wednesday"
                checked={formData.days.includes("Wednesday")}
                onChange={handleDayChange}
            />
            Środa
            </label>
            <label className="checkbox-label">
            <input
                type="checkbox"
                value="Thursday"
                checked={formData.days.includes("Thursday")}
                onChange={handleDayChange}
            />
            Czwartek
            </label>
            <label className="checkbox-label">
            <input
                type="checkbox"
                value="Friday"
                checked={formData.days.includes("Friday")}
                onChange={handleDayChange}
            />
            Piątek
            </label>
            <label className="checkbox-label">
            <input
                type="checkbox"
                value="Saturday"
                checked={formData.days.includes("Saturday")}
                onChange={handleDayChange}
            />
            Sobota
            </label>
            <label className="checkbox-label">
            <input
                type="checkbox"
                value="Sunday"
                checked={formData.days.includes("Sunday")}
                onChange={handleDayChange}
            />
            Niedziela
            </label>
        </div>
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
          step="1"
          onInput={(e) => {
            e.target.value = e.target.value.replace(/[^0-9]/g, '');
          }}
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
          min="0"
          step="1"
          onInput={(e) => {
            e.target.value = e.target.value.replace(/[^0-9]/g, '');
          }}
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
          <option value="">Zwykła</option>
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
          min="0"
          step="1"
          onInput={(e) => {
            e.target.value = e.target.value.replace(/[^0-9]/g, '');
          }}
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
