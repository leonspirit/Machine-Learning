#include <bits/stdc++.h>

#define pb push_back
#define table vector<vector<string> >

using namespace std;

struct node
{
	int attr_pick;
	string label;
	vector<node*>children;
};

int attr,rows;
node *root = NULL;
table training_data;

double entropy(int n, int arr[])
{
	bool flag[n];
	double data=n;
	memset(flag,false,sizeof flag);
	double res=0;
	
	for(int x=0;x<n;x++)
	{
		if(flag[x]==false)
		{
			flag[x]==true;
			double found=1;
			for(int y=x+1;y<n;y++)
			{
				if(arr[y]==arr[x])
				{
					flag[y]=true;
					found=found+1;
				}
			}
			double prob = found/data;
			res+= -prob * (log(prob)/log(2));
		}
	}
	return res;
}

double infogain(int n, double parent, int arr[], int kelas[])
{
	bool flag[n];
	memset(flag,false,sizeof flag);
	
	double res=0;
	for(int x=0;x<n;x++)
	{
		if(flag[x]==false)
		{
			flag[x]=true;
			int found=1;
			int temp[n];
			temp[0]=kelas[x];
			for(int y=x+1;y<n;y++)
			{
				if(arr[x]==arr[y])
				{
					flag[y]=true;
					temp[found]=kelas[y];
					found++;
				}
			}
			double entropy_now = entropy(found,temp);
			double ketemu = found, data = n;
			res+=((ketemu/data)*entropy_now);
		}
	}
	return parent-res;
}

node* build(node *p, table data_now, int record, int attribute)
{
	if(data_now.size()==0)return NULL;
	
	bool homogen=true;
	for(int x=1;x<data_now.size();x++)
	{
		if(data_now[x][attribute-1]!=data_now[0][attribute-1])
		{
			homogen=false;
			break;
		}
	}
	if(homogen)
	{
		node *temp = new node();
		temp->attr_pick=-1;
		temp->label=data_now[0][attribute-1];
		return temp;
	}
	
	double maks=-99; int ans=-1;
	for(int x=0;x<attribute-1;x++)
	{
		int arr[record], id=0, kless[record];
		for(int y=0;y<data_now.size();y++)
		{
			arr[id++]=data_now[y][x];
			kless[id++]=data_now[y][attribute-1];
		}
		double info_gain = infogain();
		if(info_gain > maks){maks=info_gain; ans=x;}
	}
	
	bool flag[record];
	memset(flag,false,sizeof flag);
	node *temp = new node();
	temp->attr_pick=ans;
	
	for(int x=0;x<record;x++)
	{
		if(flag[x]==false)
		{
			vector<string>child_data;
			flag[x]=true;
			for(int y=x;y<record;y++)
			{
				if(data_now[x][ans]==data_now[y][ans])
				{
					flag[y]=true;
					for(int z=0;z<attribute;z++)
					{
						if(z!=ans)child_data.pb(data_now[y][z]);
					}
				}
			}
		}
	}
	
	
}

int main()
{
	string data;
	ifstream Files;
	
	Files.open("train_data.txt");
	if(!Files)
	{
		cerr << "Error: Training file not found" <<endl;
		exit(-1);
	}
	
	while(getline(Files, data))
	{
		int att_count=1,last=0;
		vector<string>record;
		for(int x=0;x<data.length();x++)
		{
			if(data[x]==',')
			{
				att_count=1;
				record.pb(data.substr(last,x-last));
				last=x+1;
			}
		}
		record.pb(data.substr(last,data.length()-last));
		training_data.pb(record);
		rows++;
		attr=max(attr,att_count);
	}
	Files.close();
	
	cout<<"Training Data"<<endl;
	for(int x=0;x<min(10,(int)training_data.size());x++)
	{
		for(int y=0;y<training_data[x].size();y++)
		{
			cout<<training_data[x][y]<<" ";
		}
		cout<<endl;
	}
	
	//root = build(root, training_data, rows, attr);
	
	return 0;
}
