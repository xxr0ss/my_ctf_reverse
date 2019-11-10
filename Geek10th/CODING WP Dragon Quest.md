# CODING WP Dragon Quest

解题关键：**正确理解题目意思**（似乎理解题意是难点）

题目意思是只要有一个monster的attack power <= 0就直接输出了，即使有选择能得到**level 60+ && HP > 0**，也会输出monster's too week。coding题就不多解释了，放代码完事（由原来错误的思路重构了一下，可能看起来有点乱， 不像是我的作风，实在太累，时间也紧迫就不继续完善了）

```c
#include <stdio.h>


int nums[3][3];

void sort() {
	int i;
	int a, b, c, m;
	for (i = 0; i < 3; i++) {
		a = nums[i][0];
		b = nums[i][1];
		c = nums[i][2];
		if (a > b) { m = a; a = b; b = m; }
		if (a > c) { m = a; a = c; c = m; }
		if (b > c) { m = b; b = c; c = m; }
		nums[i][0] = a;
		nums[i][1] = b;
		nums[i][2] = c;
	}
}

int fix(int attack) {
	return attack > 0 ? attack : 0;
}

int main() {
	int i, j, in;
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 3; j++) {
			scanf("%d", &in);
			if (in <= 0) {
				printf("The monster is too weak...");
				return 0;
			}
			nums[i][j] = fix(in);
		}
	}
	sort();

	int minimum = nums[0][0] + nums[1][0] + nums[2][0];
	
	if (minimum >= 100) {
		printf("The brave died on the way to leveling...");
		return 0;
	}

	int level[27];
	int a, b, c;

	for (a = 0; a < 3; a++) {
		for (b = 0; b < 3; b++) {
			for (c = 0; c < 3; c++) {
				level[9 * a + 3 * b + c] = nums[0][a] + nums[1][b] + nums[2][c];
			}
		}
	}

	int enough = 100;
	int cnt = 0;
	for (i = 0; i < 27; i++) {
		if (level[i] < 60) {
			cnt++;
		}
		else if (level[i] < 100) {
			if (level[i] < enough) {
				enough = level[i];
			}
		}
	}

	if (cnt == 27) {
		printf("why don't give the brave a chance to level up...");
		return 0;
	}
	else {
		if (enough < 100 && enough >= 60) {
			printf("The brave still has %dHP left to face the BOSS", 100 - enough);
			return 0;
		}
		else {
			printf("The brave died on the way to leveling...");
			return 0;
		}
	}

	return 0;
}
```

