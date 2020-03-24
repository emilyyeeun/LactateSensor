package com.ese451.sensor;

import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;

public class FitnessActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_choose);
    }

    public void onButtonClick(View v) {
        Button cardio = (Button) findViewById(R.id.button2);
        Button strength = (Button) findViewById(R.id.button3);
        Button strengthTwo = (Button) findViewById(R.id.button4);

        int id = 1;
        Intent i = new Intent(this, EnterValueActivity.class);
        if (v == cardio) {
            i.putExtra("type", "cardio");
        } else if (v == strength) {
            i.putExtra("type", "strength Endurance");
        } else {
            i.putExtra("type", "strength explosiveness");
        }
        startActivityForResult(i, id);
    }


}
