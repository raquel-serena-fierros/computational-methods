function predator_prey

%cases
alpha=1;beta=1;gamma=1;

%time series
t0 = 0; tf = 30;

%initial population
y0 = [0.8;0.8];

[t,y] = ode45(@f,[t0,tf],y0,[],alpha,beta,gamma);

v1 = y(:,2); 
u1 = y(:,1); 

% phase plane
figure(1);

plot(u1,v1,'linewidth',1);

ylabel('v');
xlabel('u');

title('(u-v) Phase Plane')

% time series
figure(2);
plot(t,u1);

xlabel('t')
ylabel('u');

title('(\alpha=1,\beta=1,\gamma=1) Time Series')

end

function func = f(t,y,alpha,beta,gamma)

v = y(2);
u = y(1); 

%predator-prey system
func = [u*(1-alpha*u)-beta*u*v ; gamma*u*v-*v];

end