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
		temp->label=data_now[0][attribute-1];
		return temp;
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
