var line0,line1,acc,mag,ori,gyr,lig,pro,gra,lin,rot,ste,ret;
var ax=null,ay=null,az=null,mx=null,my=null,mz=null,oa=null,ob=null,oc=null,gx=null,gy=null,gz=null,la=null,lb=null,lc=null,pa=null,pb=null,pc=null,grx=null,gry=null,grz=null,lix=null,liy=null,liz=null,roa=null,rob=null,roc=null,rod=null,roe=null,st=null;
var notice=new android.app.Notification.Builder(context);
notice.setContentTitle("Auto.js 运行中");
notice.setContentText("正在采集传感器信息");
notice.setSmallIcon(org.autojs.autojs.R.drawable.ic_service_green);
notice.setOngoing(true);
var notim=context.getSystemService(android.app.Service.NOTIFICATION_SERVICE);
notim.notify(618,notice.build());
var server=new java.net.ServerSocket(1862,1);
var client=server.accept();
toast("Sensors server : Successfully connected to the client.");
var in_byte=client.getInputStream();
var in_char=new java.io.InputStreamReader(in_byte);
var buffer=new java.io.BufferedReader(in_char);
var out_str=client.getOutputStream();
var writer=new java.io.PrintWriter(out_str);
while(true)
{
    line0=null;
    while(line0==null)
    {
        line0=buffer.readLine();
    }
    line1=buffer.readLine();
    switch(line0)
    {
        case "read":
            switch(line1)
            {
                case "acc":
                    ret=[ax,ay,az];
                    break;
                case "mag":
                    ret=[mx,my,mz];
                    break;
                case "ori":
                    ret={"azimuth":oa,"pitch":ob,"roll":oc};
                    break;
                case "gyr":
                    ret=[gx,gy,gz];
                    break;
                case "lig":
                    ret=[la,lb,lc];
                    break;
                case "pro":
                    ret=[pa,pb,pc];
                    break;
                case "gra":
                    ret=[grx,gry,grz];
                    break;
                case "lin":
                    ret=[lix,liy,liz];
                    break;
                case "rot":
                    ret=[roa,rob,roc,rod,roe];
                    break;
                case "ste":
                    ret=st;
                    break;
            }
            writer.write(JSON.stringify(ret)+"\n");
            writer.flush();
            break;
        case "open":
            switch(line1)
            {
                case "acc":
                    acc=sensors.register("accelerometer",sensors.delay.game);
                    acc.on("change",(e,x,y,z)=>{
                        ax=x;
                        ay=y;
                        az=z;
                    });
                    console.log("Start : accelerometer");
                    break;
                case "mag":
                    mag=sensors.register("magnetic_field",sensors.delay.game);
                    mag.on("change",(e,x,y,z)=>{
                        mx=x;
                        my=y;
                        mz=z;
                    });
                    console.log("Start : magnetic_field");
                    break;
                case "ori":
                    ori=sensors.register("orientation",sensors.delay.game);
                    ori.on("change",(e,x,y,z)=>{
                        oa=x;
                        ob=y;
                        oc=z;
                    });
                    console.log("Start : orientation");
                    break;
                case "gyr":
                    gyr=sensors.register("gyroscope",sensors.delay.game);
                    gyr.on("change",(e,x,y,z)=>{
                        gx=x;
                        gy=y;
                        gz=z;
                    });
                    console.log("Start : gyroscope");
                    break;
                case "lig":
                    lig=sensors.register("light",sensors.delay.game);
                    lig.on("change",(e,x,y,z)=>{
                        la=x;
                        lb=y;
                        lc=z;
                    });
                    console.log("Start : light");
                    break;
                case "pro":
                    pro=sensors.register("proximity",sensors.delay.game);
                    pro.on("change",(e,x,y,z)=>{
                        pa=x;
                        pb=y;
                        pc=z;
                    });
                    console.log("Start : proximity");
                    break;
                case "gra":
                    gra=sensors.register("gravity",sensors.delay.game);
                    gra.on("change",(e,x,y,z)=>{
                        grx=x;
                        gry=y;
                        grz=z;
                    });
                    console.log("Start : gravity");
                    break;
                case "lin":
                    lin=sensors.register("linear_acceleration",sensors.delay.game);
                    lin.on("change",(e,x,y,z)=>{
                        lix=x;
                        liy=y;
                        liz=z;
                    });
                    console.log("Start : linear_acceleration");
                    break;
                case "rot":
                    rot=sensors.register("rotation_vector",sensors.delay.game);
                    rot.on("change",(e,x,y,z,w,u)=>{
                        roa=x;
                        rob=y;
                        roc=z;
                        rod=w;
                        roe=u;
                    });
                    console.log("Start : rotation_vector");
                    break;
                case "ste":
                    ste=sensors.register("step_counter",sensors.delay.game);
                    ste.on("change",(e,x)=>{
                        st=x;
                    });
                    console.log("Start : step_counter");
                    break;
            }
            break;
        case "close":
            switch(line1)
            {
                case "acc":
                    sensors.unregister(acc);
                    console.log("Stop : accelerometer");
                    break;
                case "mag":
                    sensors.unregister(mag);
                    console.log("Stop : magnetic_field");
                    break;
                case "ori":
                    sensors.unregister(ori);
                    console.log("Stop : orientation");
                    break;
                case "gyr":
                    sensors.unregister(gyr);
                    console.log("Stop : gyroscope");
                    break;
                case "lig":
                    sensors.unregister(lig);
                    console.log("Stop : light");
                    break;
                case "pro":
                    sensors.unregister(pro);
                    console.log("Stop : proximity");
                    break;
                case "gra":
                    sensors.unregister(gra);
                    console.log("Stop : gravity");
                    break;
                case "lin":
                    sensors.unregister(lin);
                    console.log("Stop : linear_acceleration");
                    break;
                case "rot":
                    sensors.unregister(rot);
                    console.log("Stop : rotation_vector");
                    break;
                case "ste":
                    sensors.unregister(ste);
                    console.log("Stop : step_counter");
                    break;
            }
            break;
    }
}
