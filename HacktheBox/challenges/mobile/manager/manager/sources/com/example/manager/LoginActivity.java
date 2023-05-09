package com.example.manager;

import android.content.Intent;
import android.os.Build;
import android.os.Bundle;
import android.os.StrictMode;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.SocketTimeoutException;
import java.net.URL;

/* loaded from: classes.dex */
public class LoginActivity extends AppCompatActivity {
    EditText etPassword;
    EditText etUsername;
    String url = "";

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_login);
        this.etUsername = (EditText) findViewById(R.id.etUsername);
        this.etPassword = (EditText) findViewById(R.id.etPassword);
        this.url = getIntent().getStringExtra("url");
        if (Build.VERSION.SDK_INT > 8) {
            StrictMode.setThreadPolicy(new StrictMode.ThreadPolicy.Builder().permitAll().build());
        }
        ((Button) findViewById(R.id.btnLogin)).setOnClickListener(new View.OnClickListener() { // from class: com.example.manager.LoginActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                try {
                    LoginActivity.this.login();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
        ((TextView) findViewById(R.id.tvRegister)).setOnClickListener(new View.OnClickListener() { // from class: com.example.manager.LoginActivity.2
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                Intent intent = new Intent(LoginActivity.this, RegisterActivity.class);
                intent.putExtra("url", LoginActivity.this.url);
                LoginActivity.this.startActivity(intent);
            }
        });
    }

    public void login() throws IOException {
        String str = this.url + "login.php";
        HttpURLConnection httpURLConnection = (HttpURLConnection) new URL(str).openConnection();
        httpURLConnection.setConnectTimeout(10000);
        httpURLConnection.setRequestMethod("POST");
        httpURLConnection.setRequestProperty("User-Agent", "Mozilla/5.0");
        httpURLConnection.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
        String str2 = "username=" + this.etUsername.getText().toString() + "&password=" + this.etPassword.getText().toString();
        httpURLConnection.setDoOutput(true);
        try {
            DataOutputStream dataOutputStream = new DataOutputStream(httpURLConnection.getOutputStream());
            dataOutputStream.writeBytes(str2);
            dataOutputStream.flush();
            dataOutputStream.close();
        } catch (SocketTimeoutException unused) {
            Toast.makeText(this, "Check your internet connection!", 1).show();
        }
        int responseCode = httpURLConnection.getResponseCode();
        System.out.println("\nSending 'POST' request to URL : " + str);
        System.out.println("Post parameters : " + str2);
        System.out.println("Response Code : " + responseCode);
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(httpURLConnection.getInputStream()));
        try {
            StringBuilder sb = new StringBuilder();
            while (true) {
                String readLine = bufferedReader.readLine();
                if (readLine == null) {
                    break;
                }
                sb.append(readLine);
            }
            if (sb.toString().equals("User not found!")) {
                Toast.makeText(this, "User not found!", 1).show();
            } else {
                Intent intent = new Intent(this, EditActivity.class);
                intent.putExtra("url", this.url);
                intent.putExtra("info", sb.toString());
                startActivity(intent);
            }
            bufferedReader.close();
        } catch (Throwable th) {
            try {
                bufferedReader.close();
            } catch (Throwable th2) {
                th.addSuppressed(th2);
            }
            throw th;
        }
    }
}
