package com.ese451.sensor;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.content.Intent;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void onButtonClick(View v) {
        int id = 0;
        Intent i = new Intent(this, FitnessActivity.class);
        i.putExtra("key", "enterValue");
        startActivityForResult(i, id);
    }
}
