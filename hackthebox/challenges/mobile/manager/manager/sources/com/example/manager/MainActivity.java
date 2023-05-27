package com.example.manager;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import androidx.appcompat.app.AppCompatActivity;

/* loaded from: classes.dex */
public class MainActivity extends AppCompatActivity {
    /* JADX INFO: Access modifiers changed from: protected */
    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_main);
        final EditText editText = (EditText) findViewById(R.id.etIP);
        final EditText editText2 = (EditText) findViewById(R.id.etPort);
        ((Button) findViewById(R.id.btnConnect)).setOnClickListener(new View.OnClickListener() { // from class: com.example.manager.MainActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, LoginActivity.class);
                intent.putExtra("url", "http://" + editText.getText().toString() + ":" + editText2.getText().toString() + "/");
                MainActivity.this.startActivity(intent);
            }
        });
    }
}
