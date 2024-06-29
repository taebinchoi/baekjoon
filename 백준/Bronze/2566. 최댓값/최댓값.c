#include <stdio.h>

int main(){
	int sq[9][9]={0}, max=0, row=3, col=4;
	for (int i=0; i<9; i++){
		for (int j=0; j<9; j++){
			scanf("%d", &sq[i][j]);
			if (max<sq[i][j]){
				max=sq[i][j];
				row=i+1;
				col=j+1;
			}
		}
	}

    printf("%d\n%d %d", max, row, col);
	return 0;
}