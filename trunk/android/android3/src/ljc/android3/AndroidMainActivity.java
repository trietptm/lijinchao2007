package ljc.android3;

import android.os.Bundle;
import android.app.Activity;
import android.app.Instrumentation.ActivityResult;
import android.view.Menu;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.view.*;
import android.content.Intent;
import android.app.Activity;

public class AndroidMainActivity extends Activity {

	OnClickListener listener0 = null; 
	OnClickListener listener1 = null; 
	Button button0;
	Button button1;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		listener1 = new OnClickListener(){
			public void onClick(View v){
				Intent intent1 = new Intent(AndroidMainActivity.this, ActivityRelativeLayout.class);
				startActivity(intent1);
			}
		};
		setContentView(R.layout.activity_android_main);
		button1 = (Button)findViewById(R.id.button1);
		button1.setOnClickListener(listener1);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.activity_android_main, menu);
		return true;
	}

}
