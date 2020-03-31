package com.ese451.sensor;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import org.json.*;
import com.android.volley.AuthFailureError;
import com.android.volley.RequestQueue;
import com.android.volley.Request;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.Volley;
import com.android.volley.toolbox.JsonObjectRequest;
import java.util.HashMap;
import java.util.Map;
import android.util.Log;
import android.os.StrictMode;


public class LactateActivity extends AppCompatActivity {
    private int male;
    private int age;
    private double height;
    private double weight;
    private double glucose;
    private double oxygen;
    private double heartRate;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_lactate);
        if (android.os.Build.VERSION.SDK_INT > 9)
        {
            StrictMode.ThreadPolicy policy = new
                    StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        male = EnterValueActivity.returnMale();
        age = EnterValueActivity.returnAge();
        height = EnterValueActivity.returnHeight();
        weight = EnterValueActivity.returnWeight();
        glucose = EnterValueActivity.returnGlucose();
        oxygen = EnterValueActivity.returnOxygen();
        heartRate = EnterValueActivity.returnHeartRate();
        Log.e("male", male+"");
    }

    public void onLactateButtonClick(View v) {

        postRequest();
        //getRequest();

    }


    private void postRequest() {
        Map<String, String> params = new HashMap<String, String>();
        params.put("Age", age + "");
        params.put("Male", male + "");
        params.put("Height", height + "");
        params.put("Glucose", glucose + "");
        params.put("Weight", weight + "");
        params.put("Sp02", oxygen + "");
        params.put("HeartRate", heartRate + "");

        RequestQueue requestQueue = Volley.newRequestQueue(LactateActivity.this);
        String url = "http://10.0.2.2:9000/api"; // local host
        JsonObjectRequest objectRequest = new JsonObjectRequest(
                Request.Method.POST, url, new JSONObject(params), new Response.Listener<JSONObject>(){
            TextView tv = (TextView) findViewById(R.id.lactateText);
            @Override
            public void onResponse(JSONObject response) {
                Log.v("response", response.toString());
                tv.setText(response.toString());

            }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    Log.e("error", error.toString());
                }
        })
        {
//        @Override
//        protected Map<String, String> getParams() {
//            Map<String, String> params = new HashMap<String, String>();
//            params.put("Age", age + "");
//            params.put("Male", male + "");
//            params.put("Height", height + "");
//            params.put("Glucose", glucose + "");
//            params.put("Weight", weight + "");
//            params.put("Sp02", oxygen + "");
//            params.put("HeartRate", heartRate + "");
//            return params;
//        }
//
//        @Override
//        public Map<String, String> getHeaders() throws AuthFailureError {
//            Map<String, String> params = new HashMap<String, String>();
//            params.put("Content-Type", "application/x-www-form-urlencoded");
//            return params;
//        }

    };
        requestQueue.add(objectRequest);
    }

}