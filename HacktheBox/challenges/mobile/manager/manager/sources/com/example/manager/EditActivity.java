package com.example.manager;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
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
import java.net.URL;
import org.json.JSONObject;

/* loaded from: classes.dex */
public class EditActivity extends AppCompatActivity {
    EditText etPassword;
    TextView tvID;
    TextView tvRole;
    TextView tvUsername;
    String url = "";
    String info = "";

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(R.layout.activity_edit);
        this.tvID = (TextView) findViewById(R.id.tv_etEditID);
        this.tvUsername = (TextView) findViewById(R.id.tv_etEditUsername);
        this.etPassword = (EditText) findViewById(R.id.etEditPassword);
        this.tvRole = (TextView) findViewById(R.id.tv_etEditRole);
        Intent intent = getIntent();
        this.url = intent.getStringExtra("url");
        this.info = intent.getStringExtra("info");
        printInfo();
        ((Button) findViewById(R.id.btnRegister)).setOnClickListener(new View.OnClickListener() { // from class: com.example.manager.EditActivity.1
            @Override // android.view.View.OnClickListener
            public void onClick(View view) {
                try {
                    EditActivity.this.update();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
    }

    public void printInfo() {
        try {
            JSONObject jSONObject = new JSONObject(this.info);
            this.tvID.setText(jSONObject.getString("id"));
            this.tvUsername.setText(jSONObject.getString("username"));
            this.etPassword.setText(jSONObject.getString("password"));
            this.tvRole.setText(jSONObject.getString("role"));
        } catch (Throwable unused) {
            Toast.makeText(this, "User not found!", 1).show();
            Intent intent = new Intent(this, LoginActivity.class);
            intent.putExtra("url", this.url);
            startActivity(intent);
        }
    }

    public void update() throws IOException {
        String str = this.url + "manage.php";
        HttpURLConnection httpURLConnection = (HttpURLConnection) new URL(str).openConnection();
        httpURLConnection.setRequestMethod("POST");
        httpURLConnection.setRequestProperty("User-Agent", "Mozilla/5.0");
        httpURLConnection.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
        String str2 = "username=" + this.tvUsername.getText().toString() + "&password=" + this.etPassword.getText().toString();
        httpURLConnection.setDoOutput(true);
        DataOutputStream dataOutputStream = new DataOutputStream(httpURLConnection.getOutputStream());
        try {
            dataOutputStream.writeBytes(str2);
            dataOutputStream.flush();
            dataOutputStream.close();
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
                if (sb.toString().equals("An error occurred!")) {
                    Toast.makeText(this, "An error occurred!", 1).show();
                } else {
                    Toast.makeText(this, "Password updated successfully.", 1).show();
                    Intent intent = new Intent(this, LoginActivity.class);
                    intent.putExtra("url", this.url);
                    startActivity(intent);
                }
                Log.d("rrrrrrrrrrrrrrr: ", sb.toString());
                bufferedReader.close();
            } catch (Throwable th) {
                try {
                    bufferedReader.close();
                } catch (Throwable th2) {
                    th.addSuppressed(th2);
                }
                throw th;
            }
        } catch (Throwable th3) {
            try {
                dataOutputStream.close();
            } catch (Throwable th4) {
                th3.addSuppressed(th4);
            }
            throw th3;
        }
    }
}
