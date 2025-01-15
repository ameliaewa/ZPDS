import React from 'react';
import { PDFDownloadLink } from '@react-pdf/renderer';
import { Document, Page, Text } from '@react-pdf/renderer';

const PDFGenerator = ({ mealPlan }) => {
  const generatePDF = () => (
    <Document>
      <Page size="A4">
        <Text>Jadłospis na tydzień:</Text>
        {mealPlan.days.map((day, index) => (
          <Text key={index}>{day.day}: {day.meals.join(', ')}</Text>
        ))}
        <Text>Lista zakupów:</Text>
        {mealPlan.shoppingList.map((item, index) => (
          <Text key={index}>{item}</Text>
        ))}
      </Page>
    </Document>
  );

  return (
    <PDFDownloadLink document={generatePDF()} fileName="jadlospis.pdf">
      {({ loading }) => (
        <button className="download-button">
          {loading ? 'Generowanie PDF...' : 'Pobierz PDF'}
        </button>
      )}
    </PDFDownloadLink>
  );
};

export default PDFGenerator;
