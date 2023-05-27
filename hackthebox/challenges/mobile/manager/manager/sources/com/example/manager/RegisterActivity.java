package com.example.manager;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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
public class RegisterActivity extends AppCompatActivity {
    EditText etPassword;
    EditText etUsername;
    String url = "";

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_register);
        this.etUsername = (EditText) findViewById(R.id.etUsername);
        this.etPassword = (EditText) findViewById(R.id.etPassword);
        this.url = getIntent().getStringExtra("url");
        ((Button) findViewById(R.id.btnRegister)).setOnClickListener(new View.OnClickListener() { // from class: com.example.manager.RegisterActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                try {
                    RegisterActivity.this.register();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    public void register() throws IOException {
        String str = this.url + "register.php";
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
            Toast.makeText(this, "Check your internet connection!2", 1).show();
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
            if (sb.toString().equals("Username already taken!")) {
                Toast.makeText(this, "Username already taken!", 1).show();
            } else if (sb.toString().equals("Unable to register user!")) {
                Toast.makeText(this, "Unable to register user!", 1).show();
            } else if (sb.toString().equals("An error occurred!")) {
                Toast.makeText(this, "An error occurred!", 1).show();
                Intent intent = new Intent(this, LoginActivity.class);
                intent.putExtra("url", this.url);
                startActivity(intent);
            } else {
                Toast.makeText(this, "User successfully created.", 1).show();
                Intent intent2 = new Intent(this, EditActivity.class);
                intent2.putExtra("url", this.url);
                intent2.putExtra("info", sb.toString());
                startActivity(intent2);
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
