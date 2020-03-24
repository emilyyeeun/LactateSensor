package com.ese451.sensor;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.EditText;


public class EnterValueActivity extends AppCompatActivity{
    private static int age;
    private static double height;
    private static double weight;
    private static int male;
    private static double glucose;
    private static double Sp02;
    private static double heartRate;
    private static String activity;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_enter);

        Spinner spinner = (Spinner) findViewById(R.id.gender_spinner);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource
                (this, R.array.gender_array, R.layout.gender_spinner);
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner.setAdapter(adapter);
    }

    public void onBeginButtonClick(View v) {

        activity = getIntent().getStringExtra("type");
        Spinner spinner = findViewById(R.id.gender_spinner);
        String gender = spinner.getSelectedItem().toString();
        if (gender.equals("Female")) {
            male = 0;
        } else if (gender.equals("Male")) {
            male = 1;
        }

        EditText ageEditText = (EditText) findViewById(R.id.editText2);
        String ageVal = ageEditText.getText().toString();
        age = Integer.parseInt(ageVal);

        EditText heightEditText = (EditText) findViewById(R.id.editText3);
        String heightVal = heightEditText.getText().toString();
        height = Double.parseDouble(heightVal);

        EditText weightEditText = (EditText) findViewById(R.id.editText4);
        String weightVal = weightEditText.getText().toString();
        weight = Double.parseDouble(weightVal);

        EditText oxygenEdit = (EditText) findViewById(R.id.editText5);
        String oxygenVal = oxygenEdit.getText().toString();
        Sp02 = Double.parseDouble(oxygenVal);

        EditText glucoseEdit = (EditText) findViewById(R.id.glucose);
        String glucoseVal = glucoseEdit.getText().toString();
        glucose = Double.parseDouble(glucoseVal);

        EditText heartEdit = (EditText) findViewById(R.id.heartRate);
        String heartVal = heartEdit.getText().toString();
        heartRate = Double.parseDouble(heartVal);

        int id = 3;
        Intent i = new Intent(this, LactateActivity.class);
        i.putExtra("activity", "Show Lactate");
        startActivityForResult(i, id);
    }

    public static String returnActivity() { return activity; }

    public static int returnAge() {
        return age;
    }

    public static int returnMale() {
        return male;
    }

    public static double returnHeight() { return height; }

    public static double returnGlucose() { return glucose; }

    public static double returnWeight() {
        return weight;
    }

    public static double returnOxygen() {
        return Sp02;
    }

    public static double returnHeartRate() {
        return heartRate;
    }
}
